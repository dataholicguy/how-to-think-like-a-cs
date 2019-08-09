import turtle

def make_window(colr, ttle):
    """Make a window with background color of colr and title of ttle"""
    w = turtle.Screen()
    w.title(ttle)
    w.bgcolor(colr)
    return w


def make_turtle(colr, sz):
    """Make a turtle with color of colr and size of sz. """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t


wn = make_window('lightgreen', 'House')
tess = make_turtle('blue', 3)

data = [(0, 100), (90, 100), (90, 100), (90, 100), (135, 141.2), (75, 100), (120, 100), (75, 141.2)]
for (angle, distance) in data:
    tess.left(angle)
    tess.forward(distance)

tess.hideturtle()

wn.mainloop()
