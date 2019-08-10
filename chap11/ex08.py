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
    test(cross_product([2, 3, 4], [5, 6, 7]) == [-3, 6, -3])
    test(cross_product([3, -3, 1], [4, 9, 2]) == [-15, -2, 39])


def cross_product(u, v):
    """ Return cross product of two vectors. """
    result = []
    result.append(u[1]*v[2]-u[2]*v[1])
    result.append(u[2]*v[0]-u[0]*v[2])
    result.append(u[0]*v[1]-u[1]*v[0])
    return result


test_suite()
