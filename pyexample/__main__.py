#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
from os import path
from pyexample.hello import Hello

__dir__ = path.realpath(path.dirname(__file__))
__resource__ = path.join(__dir__, 'resources')


def find_config():
	config_found = False
	con = 'config.ini'
	for filename in [con, path.join(__resource__, con)]:
		if path.exists(filename):
			print("Config found: ", filename)
			config_found = True

	if not config_found:
		raise Exception()


def use_hello_module():
	h = Hello()
	print(h.say_hello())

	if len(sys.argv) > 1:
		print("Text from resource1.dat:")
		h.say_long()


def main():
	print("Greating from __main__ func")

	use_hello_module()

	find_config()


if __name__ == "__main__":
	main()
