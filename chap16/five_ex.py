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
    r = Rectangle(Point(0, 0), 10, 5)
    test(r.area() == 50)

    test(r.perimeter() == 30)

    r = Rectangle(Point(100, 50), 10, 5)
    test(r.width == 10 and r.height == 5)
    r.flip()
    test(r.width == 5 and r.height == 10)

    r = Rectangle(Point(0, 0), 10, 5)
    test(r.contains(Point(0, 0)))
    test(r.contains(Point(3, 3)))
    test(not r.contains(Point(3, 7)))
    test(not r.contains(Point(3, 5)))
    test(r.contains(Point(3, 4.99999)))
    test(not r.contains(Point(-3, -3)))

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return '({0}, {1}, {2})'.format(self.corner, self.width, self.height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width+self.height)*2

    def flip(self):
        self.width, self.height = self.height, self.width

    def contains(self, pt):
        """ Check if a point is fall within the rectangle or not """
        if pt.x < 0 or pt.x >= self.corner.x + self.width:
            return False
        elif pt.y < 0 or pt.y >= self.corner.y + self.height:
            return False
        return True

    def is_collide(self, target):
        """ Check if my rectangle and target rectangle collided or not """
        if self.contains(target.corner):
            return True
        elif target.contains(self.corner):
            return True
        return False 

test_suite()
