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

def snowflake(t, order, size):
    """ Make turtle t draw a snowflake """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            snowflake(t, order-1, size/3)
            t.left(angle)

wn = make_window('lightgreen', 'Koch Snowflake')
tess = make_turtle('blue', 1)

for _ in range(3):
    snowflake(tess, 2, 100)
    tess.right(120)

wn.mainloop()
