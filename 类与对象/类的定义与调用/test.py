# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/25 15:24
---------------------------------------------
"""
class Force:
    def __init__(self, x, y):
        self.F_x, self.F_y = x, y

    def show(self):
        print(f'Force({self.F_x},{self.F_y})')

    def add(self, force2):
        x = self.F_x + force2.F_x
        y = self.F_y + force2.F_y
        return Force(x, y)

    def __add__(self, other):
        x = self.F_x + other.F_x
        y = self.F_y + other.F_y
        return Force(x, y)

    def __eq__(self, other):
        return (self.F_x == other.F_x) and (self.F_y == other.F_y)


f1 = Force(2, 3)
# print(f.show())
f2 = Force(1, 2)
f1 = f1 + f2
f1.show()
print(f1 == Force(3, 5))
print(f1 == f1)
