class Point:
    """ Point class represents and manipulates x, y coords """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def distance(self, target):
        """ Return distance from my point to target point """
        dx = self.x - target.x
        dy = self.y - target.y
        return (dx**2+dy**2)**0.5

    def get_line_to(self, target):
        """ Return the two coefficients of the line as
            a tuple of two values.
        """
        m = (self.y - target.y)/(self.x - target.x)
        c = self.y - m*self.x
        return (m, c)

def get_square_line(pt1, pt2):
    """ Return the two coefficients of the line
        that squared with the straight line as
        a tuple of two values.
    """
    line = pt1.get_line_to(pt2)
    m = -1 / line[0]
    mid = pt1.halfway(pt2)    # Midpoint between pt1 and pt2
    c = mid.y - m * mid.x
    return (m, c)

def get_cross_point(line1, line2):
    """ Get the cross point between two lines
        given as two tuple of two values.
    """
    (m1, c1) = line1
    (m2, c2) = line2
    x0 = (c2-c1)/(m1-m2)
    y0 = m1 * x0 + c1
    return (x0, y0)


def find_midpoint(pt1, pt2, pt3, pt4):
    """ Return coords of the midpoint of a circle,
        given 4 points fall on the circumference of a circle
    """
    line1 = get_square_line(pt1, pt2)
    line2 = get_square_line(pt1, pt3)
    return get_cross_point(line1, line2)

a = Point(2, 0)
b = Point(1, 1)
c = Point(1, -1)
d = Point(0, 0)

print('Midpoint of the circle: {0}'.format(find_midpoint(a, b, c, d)))
