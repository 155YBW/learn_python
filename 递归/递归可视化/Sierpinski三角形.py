# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/12/7 16:09
---------------------------------------------
"""
import turtle


def drawTriangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()  # 绘制需要填充色的图形(开始)
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()  # 绘制需要填充色的图形(结束)


# 规模减半函数，取中点
def getMid(p1, p2):
    return ( (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 )


def sierpinski(degree, points):
    """
    画完主三角形后，画周围3个分割出的三角形,绘制顺序：left, top, right
    :param degree:
    :param points:
    :return:
    """
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'orange']
    drawTriangle(points, colormap[degree])
    if degree > 0:
        sierpinski(degree - 1,
                   {'left': points['left'],
                    'top': getMid(points['left'], points['top']),
                    'right': getMid(points['left'], points['right'])})

        sierpinski(degree - 1,
                   {'left': getMid(points['left'], points['top']),
                    'top': points['top'],
                    'right': getMid(points['top'], points['right'])})

        sierpinski(degree - 1,
                   {'left': getMid(points['left'], points['right']),
                    'top': getMid(points['top'], points['right']),
                    'right': points['right']})


if __name__ == '__main__':
    t = turtle.Turtle()
    points = {'left': (-200, -100),
              'top': (0, 200),
              'right': (200, -100)}

    sierpinski(3, points)
    turtle.done()
