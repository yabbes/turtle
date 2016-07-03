#!/usr/bin/env python3

import turtle
wn = turtle.Screen()
wn.bgcolor("green")

jamal = turtle.Turtle()
jamal.color("white")
jamal.pensize(10)
jamal.goto(-200, -200)
print(jamal.position())

def circle(length):
    for i in range(8):
        jamal.forward(length)
        jamal.left(45)
circle(60)
jamal.color("yellow")
circle(120)
jamal.color("white")
circle(135)

wn.exitonclick()

