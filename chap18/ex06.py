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
    test(count(2, []) == 0)
    test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
    test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
    test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
    test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
    test(count("a",
         [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)

def count(target, nested_list):
    """ Return the number of occurences of target in a nested list """
    result = 0

    for e in nested_list:
        if type(e) == type([]):
            result += count(target, e)
        else:
            if e == target:
                result += 1

    return result

test_suite()
