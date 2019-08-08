# Suppose our turtle tess is at heading 0 — facing east. We execute the statement tess.left(3645).
# What does tess do, and what is her final heading?

import turtle

wn = turtle.Screen()
wn.title('Hello, Tess!')
wn.bgcolor('lightgreen')

tess = turtle.Turtle()
tess.shape('turtle')
tess.left(3645) # 3645 % 360 = 45 so tess turn left for 45 degrees

wn.mainloop()
