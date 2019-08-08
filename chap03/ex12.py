# draw a face of a clock

import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Face of a Clock')

tess = turtle.Turtle()
tess.pensize(3)
tess.color('blue')
tess.shape('turtle')
tess.stamp()

for _ in range(12):
    tess.shape('turtle')
    tess.penup()
    tess.forward(100)
    tess.pendown()
    tess.shape('classic')
    tess.forward(10)
    tess.penup()
    tess.forward(20)
    tess.shape('turtle')
    tess.stamp()
    tess.forward(-130)
    tess.left(30)

wn.mainloop()
