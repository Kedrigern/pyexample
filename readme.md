PyExample
=========

Python example project. Example of:

* Entry point (`app.py`)
* module (`pyexample`)
* module with resources (`pyexample/resources`)
* dependencies via `requirements.txt` (used in `setup.py`)
* setuptools (`setup.py`, `MANIFEST.in`)
* unit tests via standard `unittest` module


Install
-------

```
sudo dnf install pip3
sudo pip3 install git+https://github.com/Kedrigern/pyexample.git
```

`dnf` is install software for Fedora. On other OS use another app.

After git url you can specify tag:

```
sudo pip3 install git+https://github.com/Kedrigern/pyexample.git@v0.4.0
```

Run
---

```
pyexample
```

With any parameter output is quit different:

```
pyexample --foo
```

Run tests
---------

```
cd <git-repository-with-project>
python3 -m unittest
```

Create OS packages
------------------

If `pip` is not enough, you can create distribution packages.

### RPM

```
./setup.py bdist_rpm
```
### DEB

```
./setup.py --command-packages=stdeb.command bdist_deb
```


Links
-----

* [pypa/sampleproject](http://github.com/pypa/sampleproject)
* [doc manifest](https://docs.python.org/3.4/distutils/sourcedist.html#specifying-the-files-to-distribute)
* [doc additional files](https://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files)
* [Including non-Python files with setup.py](http://stackoverflow.com/questions/1612733/including-non-python-files-with-setup-py)

File hierarchy
--------------

```
├── DESCRIPTION.rst
├── MANIFEST.in
├── pyexample
│   ├── hello.py
│   ├── __init__.py
│   ├── __main__.py
│   └── resources
│       ├── config.ini
│       ├── dir
│       │   └── resource3.dat
│       ├── __init__.py
│       ├── resource1.dat
│       └── resource2.dat
├── readme.md
├── requirements.txt
├── run
├── setup.cfg
├── setup.py
└── test
    ├── __init__.py
    └── test_hello.py
```
