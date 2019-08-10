import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Handling Keypresses!")
wn.bgcolor('lightgreen')
tess = turtle.Turtle()

# The next four functions are our 'event' handlers
def h1():
    tess.forward(30)

def h2():
    tess.left(45)

def h3():
    tess.right(45)

def h4():
    wn.bye()    # close down the turtle window

# Change tess's color to Red, Green, Blue
def press_r():
    tess.color('red')

def press_g():
    tess.color('green')

def press_b():
    tess.color('blue')

# Increase or Decrease the width of tess's pen
size = 1

def press_plus():
    global size
    size += 1
    if size > 20:
        size = 20
    tess.pensize(size)

def press_minus():
    global size
    size -= 1
    if size < 1:
        size = 1
    tess.pensize(size)

# These lines "wire up" keypresses to handlers we've defined
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(press_r, 'r')
wn.onkey(press_g, 'g')
wn.onkey(press_b, 'b')
wn.onkey(press_plus, 'p')
wn.onkey(press_minus, 'm')

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.

wn.listen()
wn.mainloop()
