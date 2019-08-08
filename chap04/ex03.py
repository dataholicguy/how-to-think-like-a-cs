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

wn = make_window('lightgreen', 'Draw Regular Polygon')
tess = make_turtle('violet', 5)

def draw_poly(t, n, sz):
    """
        Make turtle t draw a regular polygon with n sides
        Each side has size of sz
    """
    for _ in range(n):
        t.forward(sz)
        t.left(360 / n)

draw_poly(tess, 8, 50)

wn.mainloop()
