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
    test(day_name(3) == 'Wednesday')
    test(day_name(6) == 'Saturday')
    test(day_name(0) == 'Sunday')
    test(day_name(42) == None)

def day_name(number):
    if number == 0:
        return 'Sunday'
    elif number == 1:
        return 'Monday'
    elif number == 2:
        return 'Tuesday'
    elif number == 3:
        return 'Wednesday'
    elif number == 4:
        return 'Thursday'
    elif number == 5:
        return 'Friday'
    elif number == 6:
        return 'Saturday'
    else:
        return None

test_suite()
