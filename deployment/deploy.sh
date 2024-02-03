#!/bin/bash
set -e

source config.sh

if confirm_action "Do you want to create the logs and run directories?"
then
    echo "Creating logs directory"
    mkdir -p $PROJECT_DIR/logs;

    echo "Creating run directory"
    mkdir -p $PROJECT_DIR/run;
fi

if confirm_action "Do you want to create/update the gunicorn binary?"
then
    echo "Creating gunicorn and binary"
    mkdir -p $PROJECT_DIR/bin;

    configure_bin_script "gunicorn_start"
fi

if confirm_action "Do you want to create/update the supervisor configs?"
then
    echo "Creating gunicorn supervisor config"
    create_supervisor_config "gunicorn_supervisor"
fi

if confirm_action "Do you want to create/update the nginx config?"
then
    echo "Creating nginx config"
    if confirm_action "Do you want to use the SSL enabled version?"
    then
        if confirm_action "Do you want to generate a certificate using Let's Encrypt?"
        then
            sudo snap install core
            sudo snap refresh core
            sudo snap install --classic certbot
            sudo certbot certonly --nginx -d $SERVER_NAME
            sudo certbot renew -d $SERVER_NAME --dry-run 
        fi
        sudo cp nginx_ssl.conf /etc/nginx/sites-available/$APP_NAME
    else
        sudo cp nginx.conf /etc/nginx/sites-available/$APP_NAME
    fi
    sudo sed -i "s|PROJECT_DIR|${PROJECT_DIR}|g" /etc/nginx/sites-available/$APP_NAME
    sudo sed -i "s|SERVER_NAME|${SERVER_NAME}|g" /etc/nginx/sites-available/$APP_NAME
fi

if confirm_action "Do you want to create/update the aliases?"
then
    echo "Removing old aliases"
    # Remove existing aliases
    sed -i '/alias gunicorn-logs/d' ~/.bashrc
    sed -i '/alias gunicorn-bin/d' ~/.bashrc
    sed -i '/alias gunicorn-conf/d' ~/.bashrc

    sed -i '/alias nginx-error-logs/d' ~/.bashrc
    sed -i '/alias nginx-access-logs/d' ~/.bashrc
    sed -i '/alias nginx-conf/d' ~/.bashrc

    sed -i '/alias restart-supervisor/d' ~/.bashrc
    sed -i '/alias restart-app/d' ~/.bashrc
    sed -i '/alias restart-nginx/d' ~/.bashrc

    sed -i '/alias status-supervisor/d' ~/.bashrc
    sed -i '/alias test-socket/d' ~/.bashrc
    sed -i '/alias sudovim/d' ~/.bashrc

    sed -i '/alias deploy-app/d' ~/.bashrc
    sed -i '/alias cd-logs/d' ~/.bashrc

    # Add new aliases
    echo "Creating new aliases"

    echo 'alias gunicorn-logs="tail -f '$PROJECT_DIR'/logs/gunicorn-error.log -n 10"' >> ~/.bashrc
    echo 'alias gunicorn-bin="vim '$PROJECT_DIR'/bin/gunicorn_start"' >> ~/.bashrc
    echo 'alias gunicorn-conf="sudo -E vim /etc/supervisor/conf.d/'$APP_NAME'-gunicorn_supervisor.conf"' >> ~/.bashrc

    echo 'alias nginx-error-logs="tail -f '$PROJECT_DIR'/logs/nginx-error.log -n 10" ' >> ~/.bashrc
    echo 'alias nginx-access-logs="tail -f '$PROJECT_DIR'/logs/nginx-access.log -n 10"' >> ~/.bashrc
    echo 'alias nginx-conf="sudo -E vim /etc/nginx/sites-available/'$APP_NAME'"' >> ~/.bashrc

    echo "alias restart-supervisor='sudo supervisorctl reread && sudo supervisorctl update'" >> ~/.bashrc
    echo "alias restart-app='sudo supervisorctl restart "$APP_NAME"'" >> ~/.bashrc
    echo "alias restart-nginx='sudo systemctl restart nginx'" >> ~/.bashrc

    echo "alias test-socket='curl --unix-socket $PROJECT_DIR/run/gunicorn.sock localhost'" >> ~/.bashrc
    echo "alias status-supervisor='sudo supervisorctl status'" >> ~/.bashrc
    echo "alias deploy-app='cd $PROJECT_DIR/deployment && bash deploy.sh'" >> ~/.bashrc
    echo "alias cd-logs='cd $PROJECT_DIR/logs'" >> ~/.bashrc
fi 

# if users says yes, create a symlink to the nginx config
if confirm_action "Do you want to create a symlink to the nginx config in sites-enabled?"
then
    # don't create a symlink if it already exists
    if [ -L /etc/nginx/sites-enabled/$APP_NAME ]
    then
        echo "Symlink already exists"
        exit 0
    else
        echo "Creating symlink"
        sudo ln -s /etc/nginx/sites-available/$APP_NAME /etc/nginx/sites-enabled  
    fi 
fi
