import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno     # Get the caller's line number.
    if did_pass:
        msg = 'Test at line {0} ok.'.format(linenum)
    else:
        msg = 'Test at line {0} FAILED.'.format(linenum)
    print(msg)

def test_suit():
    """ Run the suite of tests for code in this module (this file) """
    test(turn_clockwise('N') == 'E')
    test(turn_clockwise('W') == 'N')
    test(turn_clockwise(42) == None)
    test(turn_clockwise('rubbish') == None)

def turn_clockwise(compass_point):
    if compass_point == 'N':
        return 'E'
    elif compass_point == 'W':
        return 'N'
    elif compass_point == 'E':
        return 'S'
    elif compass_point == 'S':
        return 'W'
    else:
        return None

test_suit()
