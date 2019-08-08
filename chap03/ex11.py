# Draw a star
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.title('Star')

tess = turtle.Turtle()
tess.pensize(5)

for _ in range(5):
    tess.forward(200)
    tess.right(144)

tess.hideturtle()

wn.mainloop()
