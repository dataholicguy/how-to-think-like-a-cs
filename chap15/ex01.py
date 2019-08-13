class Point:
    """ Point class represents and manipulates x, y coords """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)


def distance(pt1, pt2):
    """ Return distance between 2 points """
    dx = pt2.x - pt1.x
    dy = pt2.y - pt1.y
    return (dx**2+dy**2) ** 0.5

p = Point(1, 10)
q = Point(5, 20)
print('Distance between {0} and {1}: {2}'.format(p, q, distance(p, q)))
