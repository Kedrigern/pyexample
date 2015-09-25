#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
from setuptools import (setup, find_packages)
from pyexample import __doc__, __author__, __version__, __license__, __email__

# Get the long description from the relevant file
here = path.abspath(path.dirname(__file__))
filepath = path.join(here, 'DESCRIPTION.rst')
with open(filepath, encoding='utf8') as f:
	long_description = f.read()

setup(
	# Basic
	name='pyexample',
	version=__version__,
	packages=find_packages(),

	# Requirements
	install_requires=[],
	extras_require={
		'dev': ['check-manifest'],
		'test': ['coverage'],
	},

	# Entry ponit
	entry_points={
		'console_scripts': [
			'pyexample = pyexample.__main__:main',
		]
	},
	# copy script run into /usr/bin,
	# but better is used entry point
	# scripts=['run'],

	# Data
	package_data={
		# If any package contains *.txt or *.rst files, include them:
		# '': ['*.txt', '*.rst'],
		# And include any *.msg files found in the 'hello' package, too:
		'pyexample': ['resources/*']
	},

	# test_suite = test.test_hello,

	# About
	author=str(__author__),
	author_email=__email__,
	description='Python example project',
	long_description=__doc__,
	license=__license__,
	keywords="python3 example",
	url='https://github.com/kedrigern/pyexample',
	classifiers=[
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
