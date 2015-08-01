#!/usr/bin/env python3

import os
import sys
from pyexample.hello import Hello


if __name__ == "__main__":
	print("Greating from main func")

	h = Hello()
	print(h.say_hello())

	if len(sys.argv) > 1:
		print("Long letter from file:")
		h.say_long()

	if not os.path.exists("config.ini"):
		print("Config file not found!")
