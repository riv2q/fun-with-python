# -*- coding: utf-8 -*-
import random

__doc__ = """bin(x)
Convert an integer number to a binary string. The result is a valid Python expression. If x is not a Python int object, it has to define an __index__() method that returns an integer.

New in version 2.6.
"""


def sample():
    """sample of `bin` usage
    """
    numbers = [random.randint(0, 100) for x in xrange(10)]
    print 'result: {result}'.format(result='OK' if all(
        [bin(n) == convert_to_binary(n) for n in numbers]) else 'BLAD')

def convert_to_binary(number):
    """converts number to binary output
    """
    binary_tab = []
    while number >= 0:
        binary_tab.insert(0, number % 2)
        number //= 2
    return '0b{binary}'.format(
        binary=''.join(map(str, binary_tab)))

sample()
