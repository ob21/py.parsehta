## On Windows

### Virtualenv

Activate virtual env : Script\activate.bat

Deactivate virtual env : Script\deactivate.bat

## On Linux

### Pre-requisites

* sudo python3 -m pip install virtualenv
* create virtual env : python3 -without pip -m venv env (without pip because blocking on Synology)
* curl https://bootstrap.pypa.io/get-pip.py | python (to install pip in it)

### Virtualenv

Activate virtual env : source env/bin/activate

Deactivate virtual env : deactivate
