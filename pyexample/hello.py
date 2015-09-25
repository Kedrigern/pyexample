#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from os import path

__dir__ = path.realpath(path.dirname(__file__))
__resource__ = path.join(__dir__, 'resources')


class Hello:
	"""
	Example class
	"""

	@staticmethod
	def say_hello():
		"""
		Basic greating from class
		"""
		return "Greating from %s class" % __class__.__name__

	@staticmethod
	def say_long():
		"""
		Iterate throw resource and print resource to the stdout
		"""
		for file in ['resource1.dat', 'resource2.dat', path.join('dir', 'resource3.dat')]:
			fullpath = path.join(__resource__, file)
			with open(fullpath) as f:
				print(f.read().strip('\n'))

	@staticmethod
	def find_config():
		"""
		Find config dir
		"""
		config_found = False
		con = 'config.ini'
		for filename in [con, path.join(__resource__, con)]:
			if path.exists(filename):
				print("Config found: ", filename)
				config_found = True

		if not config_found:
			raise Exception()


if __name__ == '__main__':
	h = Hello()
	print('Run modul hello')
	print(h.say_hello())
