import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = 'Test at line {0} ok.'.format(linenum)
    else:
        msg = 'Test at line {0} FAILED'.format(linenum)
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file) """
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)

def hours_in(total_seconds):
    """ Return the whole integer number of hours represented by a total number of seconds"""
    return total_seconds // 3600

def minutes_in(total_seconds):
    """
        Return the whole integer number of left over minutes in a total number of seconds,
        once the hours have taken out.
    """
    return (total_seconds-hours_in(total_seconds)*3600) // 60

def seconds_in(total_seconds):
    """
        Returns the left over seconds represented by a total number of seconds.
    """
    return total_seconds - hours_in(total_seconds) * 3600 - minutes_in(total_seconds) * 60

test_suite()
