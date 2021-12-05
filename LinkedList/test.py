# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/23 21:29
---------------------------------------------
"""
import orderlist
# from LinkedList.unorderList import Node

guss = orderlist.OrderedList()

guss.add(10)

guss.add(1)

guss.add(22)

print(guss.size())

print(guss.index(1))

print(guss.search(23))