# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/27 11:29
---------------------------------------------
"""
class Car:
    def __init__(self, name):
        self.name = name
        self.remain_mile = 0

    def fill_fuel(self, miles):
        self.remain_mile = miles

    def run(self, miles):
        print(self.name, end=';')
        if self.remain_mile >= miles:
            self.remain_mile -= miles
            print(f"run{miles}miles.")
        else:
            print(f'just run {self.remain_mile} miles,fuel out.')

class GasCar(Car):
    def __init__(self, name, cap):
        super().__init__(name)
        self.cap = cap

    def show(self):
        print(self.name, end='; ')
        print(self.cap)

    def fill_fuel(self, miles):
        self.remain_mile = miles*6

class ElecCar(Car):
    def fill_fuel(self, miles):
        self.remain_mile = miles*3

gcar = GasCar('BMW', 30)
gcar.show()
gcar.fill_fuel(50)
gcar.run(30)

ecar = ElecCar("mt")
ecar.fill_fuel(20)
ecar.run(80)