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
    test(remove("an", "banana") == "bana")
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Missippi")
    test(remove("eggs", "bicycle") == "bicycle")


def remove(sub, strng):
    """ Remove the first occurence of a string from another string. """
    if sub not in strng:
        return strng
    else:
        index = strng.find(sub)
        result = ''
        for i in range(index):
            result += strng[i]
        for i in range(index+len(sub), len(strng)):
            result += strng[i]
        return result

test_suite()
