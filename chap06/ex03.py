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
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)

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

def day_num(name):
    if name == 'Sunday':
        return 0
    elif name == 'Monday':
        return 1
    elif name == 'Tuesday':
        return 2
    elif name == 'Wednesday':
        return 3
    elif name == 'Thursday':
        return 4
    elif name == 'Friday':
        return 5
    elif name == 'Saturday':
        return 6
    else:
        return None

test_suite()
