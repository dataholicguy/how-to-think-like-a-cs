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


wn = make_window('lightgreen', 'Drunk Pirate')
tess = make_turtle('blue', 3)

data = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for (angle, step) in data:
    tess.right(angle)
    tess.forward(step)

wn.mainloop()
