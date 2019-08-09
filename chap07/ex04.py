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
    """ Run suite of tests for this module. """
    test(words_len_five(['hello', 'little', 'dog']) == 1)
    test(words_len_five(['five', 'six', 'seven']) == 1)


def words_len_five(words):
    """ Return how many words in a list have length 5. """
    count = 0
    for word in words:
        if len(word) == 5:
            count += 1
    return count

test_suite()
