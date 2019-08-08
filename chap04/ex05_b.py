import turtle

def make_window(colr, ttle):
    """
        Set up the window with the given background color and title
        Returns the new window
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr, sz):
    """
        Set up a turtle with the given color and pensize
        Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

wn = make_window('lightgreen', 'Draw Pretty')
tess = make_turtle('blue', 2)

size = 5
tess.right(90)
tess.speed(10)
for _ in range(103):
    tess.forward(size)
    size += 3
    tess.right(89)

wn.mainloop()
