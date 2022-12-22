create_venv="python3 -m venv venv"
install_poetry="pip install poetry"
install_package="poetry install"

eval $create_venv
eval $install_poetry
eval $install_package

echo "Done"