__doc__ = """all(iterable)
Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
New in version 2.5."""


def sample():
    """sample of `all` usage"""
