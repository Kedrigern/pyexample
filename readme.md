# PyExample

Python example project. Example of:

* Entry point (`app.py`)
* module (`pyexample`)
* module resource (`pyexample/letter.md`)
* global resource (`resource/file.dat`, `resource/config.ini`)
* setuptools (`setup.py`, `MANIFEST.in`)
* unit tests via standard `unittest` module

## Run

```
./app.py 
```

With any parametr output is quit different:

```
./app.py --foo
```

## Run tests

```
python3 -m unittest
```

## Install

```
sudo ./setup.py install
```

Install app into:

```
/usr/lib/python3.4/site-packages/
```

And allow to run by command: `app.py`

## Links

* [pypa/sampleproject](http://github.com/pypa/sampleproject)
* [doc manifest](https://docs.python.org/3.4/distutils/sourcedist.html#specifying-the-files-to-distribute)
* [doc additional files](https://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files)
* [Including non-Python files with setup.py](http://stackoverflow.com/questions/1612733/including-non-python-files-with-setup-py)

## File hiearchy

```
├── app.py
├── DESCRIPTION.rst
├── MANIFEST.in
├── pyexample
│   ├── hello.py
│   ├── __init__.py
│   └── letter.md
├── readme.md
├── resource
│   ├── config.ini
│   └── file.dat
├── setup.py
└── test
    ├── __init__.py
    └── test_hello.py
```
