#!/usr/bin/env python3

import unittest
from pyexample.hello import Hello


class MainTest(unittest.TestCase):

	def test1(self):
		h = Hello()
		returned = h.say_hello()
		expected = "Greating from Hello class" 
		self.assertEqual(returned, expected)	


if __name__ == '__main__':
	unittest.main()
