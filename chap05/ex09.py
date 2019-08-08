import turtle

def make_window(colr, ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr, sz):
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    if height >= 200:
        t.color('blue', 'red')
    elif height >= 100:
        t.color('blue', 'yellow')
    elif height < 100:
        t.color('blue', 'green')
    t.begin_fill()
    t.left(90)
    t.forward(height)
    if height > 0:
        t.write("  "+ str(height))
    elif height < 0:
        t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()

wn = make_window('lightgreen', 'Bar Chart')
tess = make_turtle('blue', 3)

xs = [48,117,200,-100,240,-30,160,260,220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()
