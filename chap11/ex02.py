import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')


tess = turtle.Turtle()
alex = tess
alex.color('hotpink')
alex.forward(100)
tess.right(90)
tess.forward(100)


print(tess is alex)
print(alex is tess)

wn.mainloop()
