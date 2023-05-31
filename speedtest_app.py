import subprocess
import os
import datetime
import platform
import netifaces
import re
import shutil
from tqdm import tqdm


def move_logs_to_saved(log_folder, log_saved_folder):
    if not os.path.exists(log_saved_folder):
        os.makedirs(log_saved_folder)

    logs = os.listdir(log_folder)
    for log_file in logs:
        if log_file.endswith(".txt"):
            source = os.path.join(log_folder, log_file)
            destination = os.path.join(log_saved_folder, log_file)
            shutil.move(source, destination)


def run_speedtest():
    command = "./speedtest"
    log_folder = "Logs"
    log_saved_folder = os.path.join(log_folder, "log_saved")

    # Move os logs antigos para a pasta "log_saved"
    move_logs_to_saved(log_folder, log_saved_folder)

    try:
        start_time = datetime.datetime.now()

        output = ""

        process = subprocess.Popen(
            command.split(), stdout=subprocess.PIPE, universal_newlines=True)

        progress_bar = tqdm(total=100, desc="Executando Speedtest")

        for line in process.stdout:
            output += line
            progress_bar.update(10)

        process.wait()
        output = output.strip()

        end_time = datetime.datetime.now()
        total_time = end_time - start_time

        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        connection_type = "WiFi" if is_wifi_connected() else "Cabo"
        wifi_frequency = get_wifi_frequency()

        os_info = platform.system() + " " + platform.release()

        log_entry = f"Data/Hora: {end_time}\n"
        log_entry += f"Tempo Total: {total_time}\n"
        log_entry += f"Conexão: {connection_type}\n"
        log_entry += f"Frequência WiFi: {wifi_frequency}\n"
        log_entry += f"Sistema Operacional: {os_info}\n"
        log_entry += f"Resultado:\n{output}\n"

        log_file = os.path.join(
            log_folder, f"speedtest_log_{end_time.strftime('%Y%m%d_%H%M%S')}.txt")

        with open(log_file, "a") as file:
            file.write(log_entry)
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
    command = "iwconfig wlp1s0"

    try:
        output = subprocess.check_output(
            command.split(), universal_newlines=True)

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
