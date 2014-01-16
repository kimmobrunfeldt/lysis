"""
Utils which depend from nothing or other functions in utils
"""

import inspect


def get_methods(obj, filter_func=None, sort_key=None, reverse=False):
    """Finds out methods of a given object.

    Args:
        filter_func: Callable function that is used to filter out methodnames.
                     Method's name is given to this function. If the return
                     value is False, method is dropped from list.
        sort_key: Key function to be given to sort.
        reverse: If True, method list is returned reversed.
    Returns:
        list. Format: [("methodname": object)]
    """
    # Get all methods of the class
    methods = inspect.getmembers(obj, predicate=inspect.ismethod)

    if filter_func is not None:
        # Keep method when filter_func(methodname) == True
        methods = [(x, y) for x, y in methods if filter_func(x)]

    if sort_key is not None:
        methods.sort(key=sort_key)

    if reverse:
        methods.reverse()

    return methods


def split_analysis_doc(doc):
    """Splits analysis docstring to header and description."""
    doc = doc.split('\n', 1)
    header = doc[0].strip()
    description = '' if len(doc) < 2 else doc[1].strip()

    return header, description
