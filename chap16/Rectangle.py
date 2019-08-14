class Point:
    """ Point class represents and manipulates x, y coords. """
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

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

# Sameness
p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1 is p2) # False => shallow equality
p3 = p1
print(p1 is p3) # True  => shallow equality - compare by references

def same_coordinates(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

print(same_coordinates(p1, p2)) # True => deep equality - compare contents

# copy.copy()   => shallow copy => can be confusing & error-prone
# copy.deepcopy() => deep copy => make 2 completely separate objects 
