APP_NAME=django-htmx-components
PROJECT_DIR=/home/ubuntu/django-htmx-components
PROJECT_SUBDIR=src
REPOSITORY_NAME=iwanalabs/django-htmx-components.git
SERVER_NAME=components.iwanalabs.com
PYTHON_VERSION=3.10

function confirm_action {
    read -p "$1 [y/n] (y)" -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]] || [[ -z $REPLY ]]
    then
        return 0
    else
        return 1
    fi
}

function configure_bin_script() {
    script_name="$1"
    cp "${script_name}" "${PROJECT_DIR}/bin/${script_name}"
    chmod u+x "${PROJECT_DIR}/bin/${script_name}"
    sudo sed -i "s|APP_NAME|${APP_NAME}|g" "${PROJECT_DIR}/bin/${script_name}"
    sudo sed -i "s|PROJECT_DIR|${PROJECT_DIR}|g" "${PROJECT_DIR}/bin/${script_name}"
    sudo sed -i "s|PROJECT_SUBDIR|${PROJECT_SUBDIR}|g" "${PROJECT_DIR}/bin/${script_name}"
}

function create_supervisor_config() {
    config_name="$1"
    sudo cp "${config_name}.conf" "/etc/supervisor/conf.d/${APP_NAME}-${config_name}.conf"
    sudo sed -i "s|APP_NAME|${APP_NAME}|g" "/etc/supervisor/conf.d/${APP_NAME}-${config_name}.conf"
    sudo sed -i "s|PROJECT_DIR|${PROJECT_DIR}|g" "/etc/supervisor/conf.d/${APP_NAME}-${config_name}.conf"
}
