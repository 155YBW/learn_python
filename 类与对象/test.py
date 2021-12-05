# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/26 19:55
---------------------------------------------
"""
class People:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return f"name:{self.name},city:{self.city}"

    def moveto(self, newcity):
        self.city = newcity

    def __lt__(self, other):
        return self.city < other.city

    __repr__ = __str__


p = list()
p.append(People("Jenny", 'Wuhan'))
p.append(People("Erica", 'Beijing'))
p.append(People("Celia", 'Guangdong'))
p.append(People("David", 'Cesuo'))
print("Original:", p)

p.sort()
print("Sorted:", p)

