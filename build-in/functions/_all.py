# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random


__doc__ = """all(iterable)
Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
New in version 2.5.
"""


def sample():
    """sample of `all` usage
    """
    elements = [random.randint(1, 100) for x in xrange(10)]
    _print_result(elements)
    _print_result(elements + [None])
    _print_result(elements + [0])
    _print_result(elements + [False])
    _print_result(elements + [True])
    _print_result(elements + [.2/3])
    _print_result(elements + [2/3])


def _print_result(elements):
    """print result
    """
    print (
        "list of elements: {elements} for function `all`"
        " results: {result}".format(
            elements=", ".join(map(str, elements)),
            result=all(elements)))


sample()
