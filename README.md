# ExpenseMan

Available at https://expenseman.cyclic.cloud/

## Setup

First, make sure you have python3, pip, and venv installed and set up.

Then, create a virtual environment for our project. Open the git repo, and then run these
commands:

```sh
python3 -m venv .venv
```

A vscode popup might show up asking you to set the environment up, click yes

Then, to activate the venv in the command line, run these commands

Linux:
```sh
source .venv/bin/activate
```

Windows:
```powershell
# In cmd.exe
.venv\Scripts\activate.bat
# Or, In PowerShell
.venv\Scripts\Activate.ps1
```

Then, to install dependencies, inside the venv, run
```sh
pip install -r requirements.txt
```

## Running

Just run the `dev.py` file to run in development mode
or run `server.sh` to run in release mode

(Release mode will not work on windows, as we're using gunicorn)

There is a `server.py` file to make cyclic.sh happy, don't use for dev stuff