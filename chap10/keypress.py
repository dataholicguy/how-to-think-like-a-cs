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

# These lines "wire up" keypresses to handlers we've defined
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.

wn.listen()
wn.mainloop()
