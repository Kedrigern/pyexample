#!/usr/bin/env python3

from setuptools import (setup, find_packages)

setup(
    # Basic
    name='pyexample',
    version='0.1.0',
    packages=find_packages(),
    scripts=['app.py'],

    # Requirements
    install_requires= [],

    # About
    author='Ondřej Profant',
    author_email='ondrej.profant@gmal.com',
    description='Python example project',
    license='Affero GNU-GPL v3',
    keywords="python3 example",
    url='https://github.com/kedrigern/pyexample',

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Natural Language :: Czech',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        ]
    )

