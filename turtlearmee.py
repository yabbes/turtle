#! /usr/bin/env python3

import turtle

class Kroete(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.x_pos = x
        self.y_pos = y

def main():
    wn = turtle.Screen()
    wn.bgcolor("grey")

    troop = list()

    for i in range(3):
       kr = Kroete(20, 3)
       troop.append(kr)

    wn.exitonclick()

if __name__ == '__main__':
    main()

