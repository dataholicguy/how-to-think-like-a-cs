# Use for loop to draw a hexagon

import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Draw a Hexagon')

tess = turtle.Turtle()
tess.pensize(3)
tess.color('red')

for _ in range(6):
    tess.forward(100)
    tess.left(60)

wn.mainloop()
