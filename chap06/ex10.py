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
    test(3 % 4 == 0)
    test(3 % 4 == 3)
    test(3 / 4 == 0)
    test(3 // 4 == 0)
    test(3+4  *  2 == 14)
    test(4-2+2 == 0)
    test(len("hello, world!") == 13)

test_suite()
