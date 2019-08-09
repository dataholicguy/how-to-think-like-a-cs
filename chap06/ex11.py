import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = 'Test at line {0} ok.'.format(linenum)
    else:
        msg = 'Test at line {0} FAILED.'.format(linenum)
    print(msg)

def test_suite():
    """ Run the suite of tests for this module (this file) """
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)

def compare(a, b):
    """
        Return 1 if a > b
        Return 0 if a == b
        Return -1 if a < b
    """
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

test_suite()
