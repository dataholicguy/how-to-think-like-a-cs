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
    test(sum_even([1, 3, 5, 7, 9]) == 0)
    test(sum_even([0, 2, 1, 100]) == 102)


def sum_even(seq):
    """ return sum of all even number in a list. """
    result = 0
    for num in seq:
        if num % 2 == 0:
            result += num
    return result

test_suite()
