create_venv="python3.10 -m venv venv"
active_venv="source venv/bin/activate"
install_poetry="pip install poetry"
install_package="poetry install"

eval $create_venv
eval $active_venv
eval $install_poetry
eval $install_package

echo "Done"