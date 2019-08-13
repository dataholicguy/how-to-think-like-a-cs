class Point:
    """ Point class represents and manipulates x, y coords """
    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)

    def reflect_x(self):
        return Point(self.x, -self.y)

p = Point(1, 10)
q = p.reflect_x()
print(q)
