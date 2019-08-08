# Use a turtle to draw the path taken by our drunk friend.

import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Draw an Octagon')

tess = turtle.Turtle()
tess.pensize(3)
tess.color('red')

angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for angle in angles:
    tess.forward(100)
    tess.right(angle)

wn.mainloop()
