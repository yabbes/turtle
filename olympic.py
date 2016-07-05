#! /usr/bin/env python3
import turtle

"""olympic rings...
http://www.blog.pythonlibrary.org/2012/08/06/python-using-turtles-for-drawing/###
"""
class OlyTurtle(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self, shape="turtle")

    def drawCircle(self, x, y, color, radius=60):
        self.penup()
        self.setposition(x, y)
        self.pendown()
        self.pensize(4)
        self.color(color)
        self.circle(radius)


    def drawOlympicSymbol(self):
        """Iterates over positions predefined
        in the array """
        positions = [(0, 0, "blue"), (-120, 0, "purple"), (60, 60, "red"),
                    (-60, 60, "yellow"), (-180, 60, "green")]
        for x, y, color in positions:
            self.drawCircle(x, y, color)

if __name__ == '__main__':
    wn = turtle.Screen()
    wn.bgcolor("lightgrey")
    t = OlyTurtle()
    t.drawOlympicSymbol()
    wn.exitonclick()
