import turtle

def make_window(colr, ttle):
    """ Make a window with color and title """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr, sz):
    """ Make a turtle with color and size """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

def koch(t, order, size):
    """
        Make turtle t draw a Koch fractal of 'order' and 'size'.
        Leave the turtle facing the same direction.
    """
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)

wn = make_window('lightgreen', 'Koch Fractal')
tess = make_turtle('blue', 1)

koch(tess, 2, 600)

wn.mainloop()
