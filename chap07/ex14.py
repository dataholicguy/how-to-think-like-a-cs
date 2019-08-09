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
    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)
    test(num_digits(100) == 3)

def num_digits(number):
    """ Return number of digits of a number. """
    if number == 0:
        return 1
    abs_num = abs(number)
    count = 0
    while abs_num > 0:
        count += 1
        abs_num = abs_num // 10

    return count

test_suite()
