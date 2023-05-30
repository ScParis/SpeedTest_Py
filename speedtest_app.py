import subprocess
import os
import datetime
import platform
import netifaces
import re


def run_speedtest():
    # Comando para executar o Speedtest CLI com a opção --accept-license
    command = "./speedtest"
    log_folder = "Logs"
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_folder, f"speedtest_log_{timestamp}.txt")

    try:
        start_time = datetime.datetime.now()

        # Executa o comando do Speedtest CLI e captura a saída
        output = subprocess.check_output(command.split())
        output = output.decode("utf-8")  # Decodifica a saída para uma string

        end_time = datetime.datetime.now()
        total_time = end_time - start_time

        # Verifica se a pasta de log existe e a cria, se necessário
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        # Obtém informações da conexão
        connection_type = "WiFi" if is_wifi_connected() else "Cabo"
        wifi_frequency = get_wifi_frequency()

        # Obtém informações do sistema operacional
        os_info = platform.system() + " " + platform.release()

        # Constrói o registro com as informações coletadas
        log_entry = f"Data/Hora: {end_time}\n"
        log_entry += f"Tempo Total: {total_time}\n"
        log_entry += f"Conexão: {connection_type}\n"
        log_entry += f"Frequência WiFi: {wifi_frequency}\n"
        log_entry += f"Sistema Operacional: {os_info}\n"
        log_entry += f"Resultado:\n{output}\n"

        # Salva o registro no arquivo de log
        with open(log_file, "a") as file:
            file.write(log_entry)
            
        print("Conteúdo de 'output':")
        print(output)
        print("Speedtest concluído com sucesso. Registro salvo em", log_file)
    except subprocess.CalledProcessError as e:
        print("Ocorreu um erro ao executar o Speedtest CLI:", e)


def is_wifi_connected():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if interface.startswith('w') or interface.startswith('wl'):
            addresses = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addresses:
                return True
    return False


def get_wifi_frequency():
    command = "iwconfig wlp1s0"  # Substitua 'wlan0' pelo nome da sua interface WiFi

    try:
        output = subprocess.check_output(
            command.split(), universal_newlines=True)

        # Use expressões regulares para encontrar a frequência da rede WiFi
        frequency_match = re.search(r'Frequency:([\d.]+) GHz', output)
        if frequency_match:
            frequency = float(frequency_match.group(1))
            return frequency
        else:
            return None
    except subprocess.CalledProcessError as e:
        print("Ocorreu um erro ao executar o comando:", e)
        return None


run_speedtest()
