# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/12/6 15:48
---------------------------------------------
"""
import turtle

t = turtle.Turtle()

t.pencolor('blue')

def drawSporal(t, lineLen):
    if lineLen > 0:
        t.forward(lineLen)
        t.right(90)
        drawSporal(t, lineLen-5)


drawSporal(t, 100)

turtle.done()
