import sys

def test(did_pass):
    """ Print the result of a test """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = 'Test at line {0} ok.'.format(linenum)
    else:
        msg = 'Test at line {0} FAILED.'.format(linenum)
    print(msg)

def test_suite():
    """ Run suite of tests for this module """
    test(r_max([2, 9, [1, 13], 8, 6]) == 13)
    test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
    test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
    test(r_max(["joe", ["sam", "ben"]]) == "sam")

def r_max(nxs):
    """
      Find the maximum in a recursive structure of lists
      within other lists.
      Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest

test_suite()
