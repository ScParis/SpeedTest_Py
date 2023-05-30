# Speedtest CLI

Este é um repositório contendo um script Python para executar o Speedtest CLI e registrar os resultados.

## Pré-requisitos

Certifique-se de ter o seguinte software instalado antes de prosseguir:

- Python 3.x
- Speedtest CLI

## Instalação

Siga as etapas abaixo para instalar o Speedtest CLI e configurar o ambiente:

1. Clone este repositório para o seu diretório local:

  ```bash
   git clone https://github.com/seu-usuario/speedtest-cli.git
  ```

2. Navegue até o diretório do repositório:

  ```bash
    cd speedtest-cli
  ```

3. Instale as dependências Python:

  ```bash
    pip install -r requirements.txt
  ```

4. Baixe e instale o Speedtest CLI:

  - Para Linux/Mac:

  ```bash
    wget https://bintray.com/ookla/download/download_file?file_path=ookla-speedtest-1.0.0-x86_64-linux.tgz -O speedtest-cli.tgz
    tar -xzf speedtest-cli.tgz
    cd speedtest-cli
    chmod +x speedtest
    sudo mv speedtest /usr/local/bin/
  ```
  - Para Windows:

    - Faça o download do arquivo executável speedtest.exe em https://www.speedtest.net/apps/cli
    - Mova o arquivo speedtest.exe para o diretório do repositório clonado.
## Uso

  Para executar o Speedtest CLI e registrar os resultados, execute o seguinte comando:

  ```bash
      python3 speedtest_app.py
  ```
    
  Os resultados do Speedtest serão exibidos no terminal e também serão registrados em um arquivo de log.

## Contribuição

  Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novos recursos.

## Licença
  Este projeto está licenciado sob a MIT License.