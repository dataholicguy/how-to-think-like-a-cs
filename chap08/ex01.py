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
    test("Python"[1] == 'y')
    test("Strings are sequences of characters."[5] == 'g')
    test(len("wonderful") == 9)
    test("Mystery"[:4] == "Myst")
    test("p" in "Pineapple")
    test("apple" in "Pineapple")
    test("pear" not in "Pineapple")
    test("apple" > "pineapple")
    test("pineapple" < "Peach")


test_suite()
