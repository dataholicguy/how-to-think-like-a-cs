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


def cesaro_torn_line(t, order, size):
    """ Make a turtle draw a cesaro torn line """
    if order == 0:
        t.forward(size)
    else:
        for angle in [85, -170, 85, 0]:
            cesaro_torn_line(t, order-1, size/3)
            t.right(angle)

def cesaro_square(t, order, size):
    """ Make a turtle draw a cesaro square """
    for _ in range(4):
        cesaro_torn_line(t, order, size)
        t.right(90)

order = int(input('Your order: '))

wn = make_window('lightgreen', 'Cesaro Recursive')
tess = make_turtle('blue', 1)
tess.speed(10)

cesaro_torn_line(tess, order, 300)

cesaro_square(tess, order, 300)

wn.mainloop()
