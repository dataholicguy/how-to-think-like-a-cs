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
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")


def reverse(strng):
    """ Return reverse version of string argument. """
    result = ''
    for i in range(len(strng)-1, -1, -1):
        result += strng[i]
    return result


def mirror(strng):
    """ Return a string that mirrors string argument. """
    reverse_str = reverse(strng)
    result = strng + reverse_str
    return result 

test_suite()
