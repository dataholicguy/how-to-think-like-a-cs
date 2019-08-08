def is_rightangled(side1, side2, side3):
    """return True if the triangle is right-angled, or False otherwise"""
    return abs(side1**2+side2**2 - side3**2) < 0.000001

print(is_rightangled(3, 4, 5))
print(is_rightangled(3, 4, 6))
