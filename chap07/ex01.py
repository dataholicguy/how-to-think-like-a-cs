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
    test(count_odd([1, 2, 3]) == 2)
    test(count_odd([0, 2, 4, 6, 8]) == 0)

def count_odd(seq):
    """ return the number of odd numbers in a list. """
    count = 0
    for num in seq:
        if num % 2 == 1:
            count += 1
    return count

test_suite()
