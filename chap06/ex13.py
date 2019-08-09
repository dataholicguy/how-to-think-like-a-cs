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
    """ Run the suite of tests for this module """
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)


def slope(x1, y1, x2, y2):
    """ return the slope of the line through the points (x1, y1) and (x2, y2) """
    return (y2-y1)/(x2-x1)

def intercept(x1, y1, x2, y2):
    """ return the y-intercept of the line through the points (x1, y1) and (x2, y2) """
    m = slope(x1, y1, x2, y2)
    return y1 - m * x1

test_suite()
