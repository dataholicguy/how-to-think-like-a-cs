import sys

def test(did_pass):
    """ Print the result of a test """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = 'Test at line {0} ok.'.format(linenum)
    else:
        msg = 'Test at line {0} FAILED.'.format(linenum)
    print(msg)

def test_suite():
    """ Run suite of tests for this module """
    test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
    test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
    test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
    test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)

def recursive_min(nested_list):
    """ Return the smallest value in a nested list """
    smallest = None
    first_time = True

    for e in nested_list:
        if type(e) == type([]):
            val = recursive_min(e)
        else:
            val = e

        if first_time or val < smallest:
            smallest = val
            first_time = False

    return smallest

test_suite()
