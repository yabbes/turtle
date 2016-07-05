#! /usr/bin/env python3
import turtle

########olympic rings...###

class OlyTurtle(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self, shape="turtle")

    def drawCircle(self, x, y, radius=50):
        self.penup()
        self.setposition(x, y)
        self.pendown()
        self.pensize(4)
        self.circle(radius)


    def drawOlympicSymbol(self):
        """Iterates over positions predefined
        in the array """
        positions = [(0, 0), (-120, 0), (60, 60),
                    (-60, 60), (-180, 60)]
        for position in positions:
            self.drawCircle(position[0], position[1])

if __name__ == '__main__':
    wn = turtle.Screen()
    t = OlyTurtle()
    t.drawOlympicSymbol()
    wn.exitonclick()
