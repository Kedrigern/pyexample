#!/usr/bin/env python3

import sys
from os import path
from pyexample.hello import Hello


def find_config():
	configFound = False
	con = 'config.ini'
	for filename in [con, path.join('resource', con)]:
		if path.exists(filename):
                	configFound = True

	if not configFound:
		raise Exception()

def use_hello_module():
	
	h = Hello()
	print(h.say_hello())

	if len(sys.argv) > 1:
		print("Long letter from file:")
		h.say_long()

def main():
	print("Greating from main func")

	use_hello_module()

	find_config()


if __name__ == "__main__":
	main()
