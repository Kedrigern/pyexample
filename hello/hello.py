#!/usr/bin/env python3

import os

__dir__ = os.path.realpath(os.path.dirname(__file__))


class Hello:
	
	def say_hello(self):
		return ("Greating from %s class" % __class__.__name__)

	def say_long(self):
		path = __dir__ + '/data/letter.md'
		with open(path) as f:
			print(f.read());


if __name__ == '__main__':
	h = Hello()
	print('Run modul hello')
	print(h.say_hello())
