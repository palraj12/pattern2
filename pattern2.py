import turtle as t

a=t.Turtle()
a.speed(100)
a1=t.Turtle()
a1.speed(100)
a.color("red")
a1.color("yellow")
from random import choice
l=[1,-1]
for x in range(1,1000):
    a.forward(x)
    a.left(179.9)
    a1.forward(x)
    a1.left(-179.9)
t.done()

