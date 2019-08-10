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
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))    # Is an empty string a palindrome?


def reverse(strng):
    """ Return reverse version of string argument. """
    result = ''
    for i in range(len(strng)-1, -1, -1):
        result += strng[i]
    return result


def is_palindrome(strng):
    """ Recognize palindromes. """
    reverse_str = reverse(strng)
    return strng == reverse_str


test_suite()
