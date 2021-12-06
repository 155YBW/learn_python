# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/12/6 15:59
---------------------------------------------
"""
import turtle


def tree(t, branchLen):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(t, branchLen - 15)
        t.left(40)
        tree(t, branchLen - 15)
        t.right(20)
        t.backward(branchLen)


t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(t, 75)
turtle.done()
