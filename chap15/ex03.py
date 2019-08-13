class Point:
    """ Point class represents and manipulates x, y coords """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)

    def slope_from_origin(self):
        return self.y / self.x

print(Point(4, 10).slope_from_origin())

print('This method fail when self.x == 0.')
print('Meaning that point lies on the y-axis.')
