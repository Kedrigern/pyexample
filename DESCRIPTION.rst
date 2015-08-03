=========
Pyexample
=========

Python3 example project. Example of:

* Entry point (`app.py`)
* module (`pyexample`)
* module with resources (`pyexample/resources`)
* setuptools (`setup.py`, `MANIFEST.in`)
* unit tests via standard `unittest` module

Install
-------

``
sudo dnf install pip3
sudo pip3 install git+https://github.com/Kedrigern/pyexample.git
``

And `pyexample` is in your system (even in `$PATH`).

`dnf` is install software for Fedora. On other OS use another app.

Update
------

``
sudo pip3 install --upgrade pyexample
``

Uninstall
---------

``
sudo pip3 uninstall -y pyexample
``

File hierarchy
--------------

On Fedora package is installed into: `/usr/lib/python3.4/site-packages`
and tree look:

``
pyexample
├── hello.py
├── __init__.py
├── __main__.py
└── resources
    ├── config.ini
    ├── __init__.py
    ├── resource1.dat
    └── resource2.dat
``


Virtual enviroment
------------------

``
sudo dnf install pip3 python3-virtualenv.noarch
sudo mkdir -p /opt/venv/pyexample
sudo chown $USER /opt/venv/pyexample
virtualenv-3.4 /opt/venv/pyexample
source /opt/virtualenv/pyexample/bin/activate
pip3 install git+https://github.com/Kedrigern/pyexample.git
deactivate
``