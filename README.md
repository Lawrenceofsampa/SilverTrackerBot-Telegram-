SilverTrackerBot Tutorial
Prerequisites / Pré-requisitos

    Debian Server
    Python 3.x
    SSH access

Step 1: Access the Server / Passo 1: Acessar o Servidor

Use SSH to connect to your Debian server:

bash

ssh username@your_server_ip -p 2222

Step 2: Update the System / Passo 2: Atualizar o Sistema

Update your package list:

bash

sudo apt update && sudo apt upgrade -y

Step 3: Install Python and Pip / Passo 3: Instalar Python e Pip

Install Python and pip:

bash

sudo apt install python3 python3-pip -y

Step 4: Clone the Repository / Passo 4: Clonar o Repositório

Clone your bot repository:

bash

git clone https://github.com/Lawrenceofsampa/SilverTrackerBot-Telegram.git

Step 5: Install Required Libraries / Passo 5: Instalar Bibliotecas Necessárias

Navigate to the bot directory and install libraries:

bash

cd SilverTrackerBot-Telegram
pip3 install -r requirements.txt

Step 6: Run the Bot / Passo 6: Executar o Bot

Run the bot:

bash

python3 bot.py

Step 7: Monitor the Bot / Passo 7: Monitorar o Bot

Check the logs to ensure the bot is running properly.


Automação do SilverTrackerBot

Para garantir que o SilverTrackerBot funcione de forma contínua, você pode usar o systemd para configurar o bot como um serviço. Siga os passos abaixo:

    Crie um arquivo de serviço:
        Execute o comando:

        bash

    sudo nano /etc/systemd/system/silvertrackerbot.service

Adicione o seguinte conteúdo ao arquivo:

ini

[Unit]
Description=Silver Tracker Bot

[Service]
ExecStart=/usr/bin/python3 /caminho/para/seu/bot.py
Restart=always
User=seu_usuario

[Install]
WantedBy=multi-user.target

Salve e saia do editor.

Ative o serviço:

bash

sudo systemctl enable silvertrackerbot.service

Inicie o serviço:

bash

sudo systemctl start silvertrackerbot.service

Verifique o status:

bash

sudo systemctl status silvertrackerbot.service

