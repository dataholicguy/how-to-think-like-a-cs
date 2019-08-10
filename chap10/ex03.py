import turtle

turtle.setup(1000, 500)
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

# Draw the second house
alex = turtle.Turtle()
alex.penup()
alex.forward(200)
alex.pendown()
draw_housing(alex)
alex.hideturtle()

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

    t1.forward(240)
    t1.left(90)
    t1.forward(50)

    t2.forward(240)
    t2.left(90)
    t2.forward(120)

    t3.forward(240)
    t3.left(90)
    t3.forward(190)


draw_traffic()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape('circle')
tess.shapesize(3)
tess.fillcolor('green')

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:      # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor('orange')
        t1.hideturtle()
        t2.showturtle()
        t3.hideturtle()
        state_num = 1
    elif state_num == 1:    # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor('red')
        t1.hideturtle()
        t2.hideturtle()
        t3.showturtle()
        state_num = 2
    else:                   # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor('green')
        t1.showturtle()
        t2.hideturtle()
        t3.hideturtle()
        state_num = 0

def auto():
    advance_state_machine()
    wn.ontimer(auto, 1000)

auto()
wn.mainloop()
