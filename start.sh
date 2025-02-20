# Install brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Install Python
brew install python
# Set up Python environment
python3 -m venv venv
# Activate the virtual environment
source venv/bin/activate
# Install required packages
pip install -r requirements.txt