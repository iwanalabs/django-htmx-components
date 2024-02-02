#!/bin/bash
set -e

source config.sh

if confirm_action "Do you want to download and install updates?"
then
    echo "Updating system"
    sudo apt update && sudo apt upgrade -y
fi

if confirm_action "Do you want to download updates automatically?"
then
    echo "Installing unattended-upgrades"
    sudo apt install unattended-upgrades apt-listchanges
    sudo dpkg-reconfigure -plow unattended-upgrades

    if ! grep -q 'Unattended-Upgrade::Automatic-Reboot "true";' /etc/apt/apt.conf.d/50unattended-upgrades; 
    then
        echo 'Unattended-Upgrade::Automatic-Reboot "true";' | sudo tee -a /etc/apt/apt.conf.d/50unattended-upgrades
    fi

    if ! grep -q 'Unattended-Upgrade::Automatic-Reboot-Time "05:00";' /etc/apt/apt.conf.d/50unattended-upgrades; 
    then
        echo 'Unattended-Upgrade::Automatic-Reboot-Time "05:00";' | sudo tee -a /etc/apt/apt.conf.d/50unattended-upgrades
    fi
fi

if confirm_action "Do you want to create a SSH key for deployment?"
then
    echo "Creating SSH key"
    ssh-keygen -t ed25519 -C "dylanjcastillo@gmail.com"
    touch ~/.ssh/config 
    chmod 600 ~/.ssh/config 
    cat >> ~/.ssh/config <<EOF
Host github-$APP_NAME 
    HostName github.com 
    AddKeysToAgent yes 
    PreferredAuthentications publickey 
    IdentityFile ~/.ssh/id_ed25519
EOF
    echo "Copy the following key to your repository's deploy keys:"
    cat ~/.ssh/id_ed25519.pub
fi

if confirm_action "Do you want to clone the repository?"
then
    echo "Cloning repository"
    git clone git@github-$APP_NAME:$REPOSITORY_NAME
fi

if confirm_action "Do you want to install python?"
then
    echo "Installing python"
    sudo apt install software-properties-common -y && \
    sudo add-apt-repository ppa:deadsnakes/ppa && \
    sudo apt update && \
    sudo apt install python$PYTHON_VERSION python$PYTHON_VERSION-venv -y
fi

if confirm_action "Do you want to install redis?"
then
    curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

    echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

    sudo apt-get update
    sudo apt-get install redis
    sudo systemctl enable --now redis-server
fi

if confirm_action "Do you want to install supervisor and nginx?"
then
    echo "Installing supervisor and nginx"
    sudo apt install supervisor nginx -y
    echo "Enabling supervisor"
    sudo systemctl enable supervisor && sudo systemctl start supervisor
    sudo usermod -aG ubuntu www-data
fi

if confirm_action "Do you want to install your .vimrc?"
then
    echo "Installing .vimrc"
    curl https://gist.githubusercontent.com/dylanjcastillo/7533db336820a66d11514c9c139e212e/raw/d1cce4a19f129be04db8d539e7d8f09e7d3fcbea/.vimrc > ~/.vimrc

    # Check if the .vim directory exists, and create it if it doesn't
    if [ ! -d "/home/ubuntu/.vim" ]; then
        mkdir /home/ubuntu/.vim
    fi

    sudo chown ubuntu:ubuntu /home/ubuntu/.vim/ -R
    echo 'alias sudovim="sudo -E vim"' >> ~/.bashrc && source ~/.bashrc
fi


if confirm_action "Do you want to install poetry?"
then
    echo "Installing poetry"
    curl -sSL https://install.python-poetry.org | python3 -
    echo "export PATH="/home/ubuntu/.local/bin:$PATH"" >> ~/.bashrc 
    /home/ubuntu/.local/bin/poetry config virtualenvs.in-project true
    echo "Remember to source ~/.bashrc for changes to take effect"
fi

if confirm_action "Do you want to initialize and install the required packages in the virtual environment?"
then
    echo "Initializing virtual environment"
    cd $PROJECT_DIR
    /home/ubuntu/.local/bin/poetry env use $(which python$PYTHON_VERSION)
    /home/ubuntu/.local/bin/poetry install --without dev
fi
