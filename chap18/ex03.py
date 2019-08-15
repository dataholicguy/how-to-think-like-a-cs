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

def draw_sierpinski(t, length, depth):
    if depth==0:
        for i in range(0,3):
            t.fd(length)
            t.left(120)
    else:
        draw_sierpinski(t, length/2,depth-1)
        t.forward(length/2)
        draw_sierpinski(t, length/2,depth-1)
        t.forward(-length/2)
        t.left(60)
        t.forward(length/2)
        t.right(60)
        draw_sierpinski(t, length/2,depth-1)
        t.left(60)
        t.forward(-length/2)
        t.right(60)


depth = int(input('Depth: '))

wn = make_window('lightgreen', 'Sierpinski Triangle')
tess = make_turtle('blue', 1)
tess.speed('fastest')

draw_sierpinski(tess, 200, depth)

wn.mainloop()
