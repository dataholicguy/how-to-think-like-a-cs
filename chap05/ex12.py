def is_rightangled(side1, side2, side3):
    sides = [side1, side2, side3]
    sides.sort()
    return abs(sides[0]**2+sides[1]**2-sides[2]**2) < 0.000001

print(is_rightangled(3, 5, 4))
print(is_rightangled(3, 6, 5))
