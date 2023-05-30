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

  - Para Mac:

  ```bash
    Download: https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-macosx-universal.tgz
  ```


  ```bash
  $ brew tap teamookla/speedtest
  $ brew update
  # Example how to remove conflicting or old versions using brew
  # brew uninstall speedtest --force
  # brew uninstall speedtest-cli --force
  $ brew install speedtest --force
  ```
  Caso a instalação seja feita pelo brew, você sempre terá a versão mais atual do Speedtest CLI. Atualize o brew sempre que puder.


  - Para Ubuntu/Debian:

    Download para Linux   

  ```bash
    i386 - https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-linux-i386.tgz
    x86_64 - https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-linux-x86_64.tgz
    armel - https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-linux-armel.tgz
    armhf - https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-linux-armhf.tgz
    aarch64 - https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-linux-aarch64.tgz
  ```

  ```bash
    ## If migrating from prior bintray install instructions please first...
    # sudo rm /etc/apt/sources.list.d/speedtest.list
    # sudo apt-get update
    # sudo apt-get remove speedtest
    ## Other non-official binaries will conflict with Speedtest CLI
    # Example how to remove using apt-get
    # sudo apt-get remove speedtest-cli
    $ sudo apt-get install curl
    $ curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | sudo bash
    $ sudo apt-get install speedtest
  ```

  ```bash
    wget https://bintray.com/ookla/download/download_file?file_path=ookla-speedtest-1.0.0-x86_64-linux.tgz -O speedtest-cli.tgz
    tar -xzf speedtest-cli.tgz
    cd speedtest-cli
    chmod +x speedtest
    sudo mv speedtest /usr/local/bin/
  ```
  - Para Ubuntu/Debian
  
  ```bash
    ## If migrating from prior bintray install instructions please first...
    # sudo rm /etc/yum.repos.d/bintray-ookla-rhel.repo
    # sudo yum remove speedtest
    ## Other non-official binaries will conflict with Speedtest CLI
    # Example how to remove using yum
    # rpm -qa | grep speedtest | xargs -I {} sudo yum -y remove {}
    $ curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.rpm.sh | sudo bash
    $ sudo yum install speedtest
  ```
  - Para FreeBSD

  Download para FreeBSD

  ```bash
    Disponível apenas para x86_64 - https://www.speedtest.net/pt/apps/cli#freebsd-flyout
  ```

  ```bash
    $ sudo pkg update && sudo pkg install -g libidn2 ca_root_nss
    # Example how to remove conflicting or old versions using pkg
    # sudo pkg remove speedtest
    # freeBSD 12 install
    $ sudo pkg add "https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-freebsd12-x86_64.pkg"
    # freeBSD 13 install
    $ sudo pkg add "https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-freebsd13-x86_64.pkg"
  ```
  - Para Windows:

    - Faça o download do arquivo executável speedtest.exe em https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-win64.zip
    
## Uso

>**Certifique-se de ter o Speedtest CLI instalado corretamente e que o arquivo speedtest_app.py esteja no mesmo diretório do executável do Speedtest CLI. Em seguida, execute o script Python usando o comando:**{.is-info}

  
  Para executar o Speedtest CLI e registrar os resultados, execute o seguinte comando:

  ```bash
      python3 speedtest_app.py
  ```
    
  Os resultados do Speedtest serão exibidos no terminal e também serão registrados em um arquivo de log.

## Contribuição

  Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novos recursos.

## Licença
  Este projeto está licenciado sob a [MIT License](https://github.com/ScParis/SpeedTest_Py/blob/main/LICENSE).
