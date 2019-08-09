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
    """ Run the suite of tests for this module. """
    test(is_even(2) == True)
    test(is_even(1) == False)

def is_even(number):
    """
        Return True if the argument is an even number
        Return False if it is odd
    """
    return number % 2 == 0

test_suite()
