# -*- coding: utf-8 -*-


__doc__ = """basestring()
This abstract type is the superclass for str and unicode. It cannot be called or instantiated, but it can be used to test whether an object is an instance of str or unicode. isinstance(obj, basestring) is equivalent to isinstance(obj, (str, unicode)).

New in version 2.3.
"""


def sample():
    """sample of `basestring` usage
    """
    to_check = ['text', u'unicode',  None, 0, False, True, .2/3, 2/3, object] 
    map(_print_result, to_check)


def _print_result(element):
    """print result
    """
    print ("{val} is type: {element_type}, and isinstance({val}, basestring)"
           " results: {result}".format(
               val=element, element_type=type(element),
               result=isinstance(element, basestring)))


sample()
