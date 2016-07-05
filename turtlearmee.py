#! /usr/bin/env python3

import turtle

class Kroete(turtle.Turtle):
    def __init__(self, x, y, color):
        turtle.Turtle.__init__(self)
        self.setx = x
        self.sety = y
        self.pencolor = color

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
    for i in range(4):
       kr = Kroete(20+(20+i*2), 3, colors[i])
       troop.append(kr)

    for k in troop:
        k.simpleMove(90, 60)

    wn.exitonclick()

if __name__ == '__main__':
    main()
