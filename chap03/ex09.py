# Draw regular polygon with 18 sides

import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Draw an Regular Polygon with 18 Sides')

tess = turtle.Turtle()
tess.pensize(3)
tess.color('red')

# the angle to find
angle = 360 / 18    # because the polygon has 18 sides

for _ in range(18):
    tess.forward(50)
    tess.left(angle)

wn.mainloop()
