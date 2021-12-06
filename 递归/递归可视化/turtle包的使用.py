# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/12/6 15:31
---------------------------------------------
"""
import turtle


def square():
    t = turtle.Turtle()

    for i in range(4):
        t.forward(100)
        t.right(90)

    turtle.done()


def star():
    t = turtle.Turtle()

    t.pencolor('blue')
    t.pensize(3)
    for i in range(5):
        t.forward(100)
        t.right(144)
    t.hideturtle()  # 画完后隐藏乌龟

    turtle.done()


if __name__ == '__main__':
    star()
