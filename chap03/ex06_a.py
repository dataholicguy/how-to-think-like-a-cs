# Use for loops to make a turtle draw an equilateral triangle

import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Equilateral Triangle')

tess = turtle.Turtle()
tess.pensize(3)
tess.color('red')

for _ in range(3):
    tess.forward(100)
    tess.left(120)

wn.mainloop()
