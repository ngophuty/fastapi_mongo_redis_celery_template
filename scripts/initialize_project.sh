apt_update="sudo apt-get update"
install_env="sudo apt install python3.10-venv"
create_venv="python3.10 -m venv venv"
active_venv="source venv/bin/activate"
install_poetry="pip install poetry"
install_package="poetry install"


eval $apt_update
eval $install_env
eval $create_venv
eval $active_venv
eval $install_poetry
eval $install_package

echo "Done"