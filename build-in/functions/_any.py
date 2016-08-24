# -*- coding: utf-8 -*-
from __future__ import unicode_literals


__doc__ = """any(iterable)
Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
New in version 2.5.
"""

def sample():
    """sample of `any` usage
    """
    elements = [None, False]
    check_values = ['text', None, 0, False, True, 2./3, 2/3, object]
    for check_value in check_values:
        _print_result(elements + [check_value])


def _print_result(elements):
    """print result
    """
    print (
        "list of elements: {elements} for function `all`"
        " results: {result}".format(
            elements=", ".join(map(str, elements)),
            result=any(elements)))


sample()
