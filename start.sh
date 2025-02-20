# Install brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Install Python
brew install python
# Set up Python environment
python3 -m venv env
# Activate the virtual environment
source install.sh
# Install required packages
pip install -r requirements.txt