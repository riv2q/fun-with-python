# -*- coding: utf-8 -*-
from __future__ import print_function
import random

__doc__ = """bin(x)
Convert an integer number to a binary string. The result is a valid Python expression. If x is not a Python int object, it has to define an __index__() method that returns an integer.

New in version 2.6.
"""


class memorize(dict):
    """cache decorator
    """
    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.function(*key)
        return result


def sample():
    """sample of `bin` usage
    """
    numbers = [random.randint(0, 100) for x in xrange(10)]
    map(lambda x: print(bin(x), ' == ', convert_to_binary(x)), numbers)
    print('result: {result}'.format(result='OK' if all(
        [bin(n) == convert_to_binary(n) for n in numbers]) else 'BLAD'))


@memorize
def convert_to_binary(number):
    """converts number to binary output
    """
    binary_tab = []
    while number:
        binary_tab.insert(0, number % 2)
        number //= 2
    return '0b{binary}'.format(
        binary=''.join(map(str, binary_tab or [0])))

sample()
