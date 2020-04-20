#!/usr/bin/env python3

import unittest
from pyexample.hello import Hello


class MainTest(unittest.TestCase):

	def test1(self):
		h = Hello()
		returned = h.say_hello()
		expected = "Greating from Hello class" 
		self.assertEqual(returned, expected)	

	def test2(self):
		h = Hello()
		returned = h.say_long()
		contains = ["pyexample resource1", "pyexample resource2", "pyexample resource3"]
		for c in contains:
			self.assertIn(c, returned)

if __name__ == '__main__':
	unittest.main()
