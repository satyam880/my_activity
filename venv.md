# Install venv
- pip install virtualenv

# Create venv
- python3 -m venv .venv

# Workon .venv
- source .venv/bin/activate

# Install packages in venv
- pip install django

# Display list of packages installed
- pip freeze

# Make requirements.txt of installed packages
- pip freeaze>requirements.txt

# Install packages from requiremnts.txt
- pip install -r requirements.txt

# Deactivate venv
- deactivate