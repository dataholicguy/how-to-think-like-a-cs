# Use for loop to draw an Octagon

import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Draw an Octagon')

tess = turtle.Turtle()
tess.pensize(3)
tess.color('red')

for _ in range(8):
    tess.forward(100)
    tess.left(45)

wn.mainloop()
