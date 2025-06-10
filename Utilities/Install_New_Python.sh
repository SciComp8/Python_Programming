# Method 1
brew install python@3.10
brew link --overwrite python@3.10

# Method 2
# Ref: https://github.com/pyenv/pyenv?tab=readme-ov-file#switch-between-python-versions
pyenv install --list | grep "3.10" # List available Python versions
pyenv uninstall 3.8.18
pyenv install 3.10.9
pyenv global 3.10.13 # Set it as the global version
python --version 
