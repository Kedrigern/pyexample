#!/usr/bin/env python3

from hello.hello import Hello

if __name__ == "__main__":
	print("Greating from main func")

	h = Hello()
	print(h.say_hello())
