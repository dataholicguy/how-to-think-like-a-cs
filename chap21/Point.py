class Point:
    """ Point class """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)

    # Operator overloading
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __mul__(self, other):
        return (self.x*other.x + self.y*other.y)

    def __rmul__(self, other):
        # Scalar multiplication
        return Point(self.x * other, self.y * other)

    # Polymorphism (duck typing rule)
    def reverse(self):
        (self.x, self.y) = (self.y, self.x)

p = Point(10, 3)
q = Point(20, 5)
print('P: {0}'.format(p))
print('Q: {0}'.format(q))

sum = p + q
print('{0} + {1} = {2}'.format(p, q, sum))

product = p * q
print('{0} * {1} = {2}'.format(p, q, product))

scalar = 3 * p
print('{0} * {1} = {2}'.format(3, p, scalar))

# Polymorphism
def multadd(x, y, z):
    return x * y + z

p1 = Point(3, 4)
p2 = Point(5, 7)
print(multadd(2, p1, p2))
print(multadd(p1, p2, 1))

# Duck typing rule
def front_and_back(front):
    import copy
    back = copy.copy(front)
    back.reverse()
    print('{0}{1}'.format(front, back))

front_and_back(p1)
