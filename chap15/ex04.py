class Point:
    """ Point class represents and manipulates x, y coords """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)

    def get_line_to(self, target):
        """ Return the two coefficients of the line as
            a tuple of two values.
        """
        m = (self.y - target.y)/(self.x - target.x)
        c = self.y - m*self.x
        return (m, c)

print(Point(4, 11).get_line_to(Point(6, 15)))

print('This method will fail when 2 points are the same.')
