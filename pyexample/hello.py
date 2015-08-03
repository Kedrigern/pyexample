#!/usr/bin/env python3

from os import path

__dir__ = path.realpath(path.dirname(__file__))
__resource__ = path.join(__dir__, 'resources')


class Hello:
    def say_hello(self):
        return ("Greating from %s class" % __class__.__name__)

    def say_long(self):
        file = path.join(__resource__, 'resource1.dat')
        with open(file) as f:
            print(f.read())


if __name__ == '__main__':
    h = Hello()
    print('Run modul hello')
    print(h.say_hello())
