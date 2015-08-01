#!/usr/bin/env python3

import sys
from hello.hello import Hello


if __name__ == "__main__":
	print("Greating from main func")

	h = Hello()
	print(h.say_hello())

	if len(sys.argv) > 1:
		print("Long letter from file:")
		h.say_long()
