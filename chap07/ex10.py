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
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))


def sqrt(n):
    """ Return square root of a number using Newton's method. """
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.001:
            return better
        approx = better

def is_prime(number):
    count = 0
    for i in range(1, round(sqrt(number))+1):
        if number % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False

test_suite()
