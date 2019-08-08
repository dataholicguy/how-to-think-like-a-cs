# Use for loops to make a turtle draw a square
import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Draw a Square')

tess = turtle.Turtle()
tess.pensize(3)
tess.color('red')

for _ in range(4):
    tess.forward(100)
    tess.left(90)

wn.mainloop()
