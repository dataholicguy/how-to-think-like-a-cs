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
    test(sum_not_first_even([1, 10, 20, 5, 100]) == 126)
    test(sum_not_first_even([1, 3, 5, 7, 9]) == 25)


def find_first_even(seq):
    """ Return first even number in a list. """
    first_even = 0
    for num in seq:
        if num % 2 == 0:
            first_even = num
            break
    return first_even


def sum_not_first_even(seq):
    """ Return sum of all elements in a list up to but not including the first even number. """
    result = 0
    for num in seq:
        result += num
    first_even = find_first_even(seq)
    result -= first_even
    return result

test_suite()
