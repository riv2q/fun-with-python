# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import decimal


__doc__ = """abs(x)
Return the absolute value of a number. The argument may be a plain or long
integer or a floating point number. If the argument is a complex number,
its magnitude is returned.
"""


def sample():
    """sample of `abs` usage
    """
    list_of_values = [
        1, 2, -32, float("-123.22"), decimal.Decimal("-32.33"), -2.3]
    result = map(abs, list_of_values)
    types_result = map(type, result)
    print result
    print types_result
