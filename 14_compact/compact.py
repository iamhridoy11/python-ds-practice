def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    newlist = []
    while(None in lst):
        lst.remove(None)
        lst.remove('')
        lst.remove([])
        lst.remove(False)
        lst.remove(())
    return lst

result = compact([0, 1, 2, '', [], False, (), None, 'All done'])
print(result)
