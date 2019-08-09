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
    """ Run suite of tests for this module. """
    test(sum_negative([1, 2, 3, 4, 5]) == 0)
    test(sum_negative([-1, 2, 10, -5, 20]) == -6)


def sum_negative(seq):
    """ Return sum of all negative numbers in a list. """
    result = 0
    for num in seq:
        if num < 0:
            result += num
    return result

test_suite()
