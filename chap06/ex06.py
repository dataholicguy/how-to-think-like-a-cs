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
    """ Run the suite of tests for code in this module (this file) """
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(days_in_month("Machine Learning") == None)

def days_in_month(name):
    if name == 'January' or name == 'March' or name == 'May' or name == 'July' or name == 'August' or name == 'October' or name == 'December':
        return 31
    elif name == 'April' or name == 'June' or name == 'September' or name == 'November':
        return 30
    elif name == 'February':
        return 28
    else:
        return None

test_suite()
