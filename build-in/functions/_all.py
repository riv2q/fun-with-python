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
    to_check = ['text', u'unicode',  None, 0, False, True, .2/3, 2/3, object]
    map(_print_result, [elements + [el] for el in to_check])


def _print_result(elements):
    """print result
    """
    print (
        "list of elements: {elements} for function `all`"
        " results: {result}".format(
            elements=", ".join(map(str, elements)),
            result=all(elements)))


sample()
