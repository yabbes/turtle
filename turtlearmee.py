#! /usr/bin/env python3

import turtle

class Kroete(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.x_pos = x
        self.y_pos = y

    def simpleMove(length, angle):
        self.forward(length)
        self.left(angle)
        self.forward(length)
        self.left(angle)

def main():
    wn = turtle.Screen()
    wn.bgcolor("green")

    troop = list()

    for i in range(4):
       kr = Kroete(20+(i*2), 3)
       troop.append(kr)

    for k in kr:
        k.simpleMove(90, 45)

    wn.exitonclick()

if __name__ == '__main__':
    main()

