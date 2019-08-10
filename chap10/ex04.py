import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Traffic Light")
wn.bgcolor('lightgreen')

def draw_housing(t):
    """ Draw a nice housing to hold the traffic lights """
    t.pensize(3)
    t.color('black', 'darkgrey')
    t.begin_fill()
    t.forward(80)
    t.left(90)
    t.forward(200)
    t.circle(40, 180)
    t.forward(200)
    t.left(90)
    t.end_fill()

tess = turtle.Turtle()
draw_housing(tess)
tess.hideturtle()

def make_turtle(colr, sz, shape):
    """ Make a new turtle. """
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.shape(shape)
    t.shapesize(sz)
    t.fillcolor(colr)
    return t

t1 = make_turtle('green', 3, 'circle')
t2 = make_turtle('orange', 3, 'circle')
t3 = make_turtle('red', 3, 'circle')

def draw_traffic():

    t1.forward(40)
    t1.left(90)
    t1.forward(50)

    t2.forward(40)
    t2.left(90)
    t2.forward(120)

    t3.forward(40)
    t3.left(90)
    t3.forward(190)


draw_traffic()


state_num = 0

def advance_state_machine():
    global state_num
    t1.showturtle()
    t2.showturtle()
    t3.showturtle()
    if state_num == 0:
        t1.fillcolor('Khaki')
        t2.fillcolor('orange')
        t3.fillcolor('Light Salmon')
        state_num = 1
    elif state_num == 1:
        t1.fillcolor('Khaki')
        t2.fillcolor('Pale Goldenrod')
        t3.fillcolor('red')
        state_num = 2
    else:
        t1.fillcolor('green')
        t2.fillcolor('Pale Goldenrod')
        t3.fillcolor('Light Salmon')
        state_num = 0

def auto():
    advance_state_machine()
    wn.ontimer(auto, 1000)

auto()

wn.mainloop()
