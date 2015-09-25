#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
from os import path
from pyexample.hello import Hello
from pyexample import __version__

__dir__ = path.realpath(path.dirname(__file__))
__resource__ = path.join(__dir__, 'resources')


def use_hello_module():
	h = Hello()
	print(h.say_hello())

	h.find_config()

	if len(sys.argv) > 1:
		print("Text from resource1.dat:")
		h.say_long()


def main():
	print("Greating from __main__ func")

	use_hello_module()

	print("Version: %s" % __version__)


if __name__ == "__main__":
	main()
