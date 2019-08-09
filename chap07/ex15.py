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
    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)


def num_even_digits(number):
    if number == 0:
        return 1
    count = 0
    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            count += 1
        number = number // 10
    return count

test_suite()
