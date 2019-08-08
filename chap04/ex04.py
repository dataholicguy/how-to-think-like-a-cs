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

def draw_square(t, sz):
    """
        Make turtle t draw a square of sz.
    """
    for _ in range(4):
        t.forward(sz)
        t.left(90)

wn = make_window('lightgreen', 'Draw Pretty')
tess = make_turtle('blue', 3)

for _ in range(20):
    draw_square(tess, 100)
    tess.left(18)

wn.mainloop()
