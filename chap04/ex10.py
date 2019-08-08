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

def draw_star(t, sz):
    """Make turtle t draw a star, where the length of each side is 100 units """
    for _ in range(5):
        t.forward(sz)
        t.right(144)

wn = make_window('lightgreen', 'Draw 5 Stars')
tess = make_turtle('violet', 3)

for _ in range(5):
    draw_star(tess, 100)
    tess.penup()
    tess.forward(350)
    tess.right(144)
    tess.pendown()

wn.mainloop()
