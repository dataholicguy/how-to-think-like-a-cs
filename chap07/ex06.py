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
    test(words_sam(['samuel', 'samson', 'bigsam']) == 2)
    test(words_sam(['machine', 'artificial', 'data']) == 0)


def words_sam(words):
    """ Return number of words in a list and including the first occurence of the word 'sam'. """
    count = 0
    for word in words:
        if ('sam' in word) and (word.index('sam') == 0):
            count += 1
    return count

test_suite()
