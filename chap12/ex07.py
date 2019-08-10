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
    """ Run the suite of tests for this module.
    """
    test(myreplace(",", ";", "this, that, and some other thing") ==
                         "this; that; and some other thing")
    test(myreplace(" ", "**",
                     "Words will now      be  separated by stars.") ==
                     "Words**will**now**be**separated**by**stars.")

def myreplace(old, new, s):
    """ replace all old characters by new characters in a string. """
    words = s.split(old)
    new_words = []
    for word in words:
        if word:
            new_words.append(word)
    return new.join(new_words)


test_suite()
