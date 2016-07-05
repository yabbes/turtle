#! /usr/bin/env python3

import turtle
import random

class Kroete(turtle.Turtle):
    def __init__(self, x, y, color):
        turtle.Turtle.__init__(self)
        self.setposition(x,y)
        self.color(color)
        self.pensize(5)

    def simpleMove(self, length, angle):
        self.forward(length)
        self.left(angle)
        self.forward(length)
        self.left(angle)

def main():
    wn = turtle.Screen()
    wn.bgcolor("green")

    troop = list()
    colors = ["red", "blue", "yellow", "black"]
    for i in range(8):
       kr = Kroete(20+(20+i*2), 3+i*10, colors[random.randint(0,3)])
       troop.append(kr)

    for k in troop:
        k.simpleMove(90, 60)
        k.circle(100)
        k.left(80)
        k.forward(200)
        k.circle(200)
        k.left(50)
        k.forward(80)
        k.circle(60)


    wn.exitonclick()

if __name__ == '__main__':
    main()
