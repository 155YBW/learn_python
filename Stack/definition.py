# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/9 9:33
---------------------------------------------
"""
class Stack:
    def __init__(self):
        self.items = []

    # 查看是否为空
    def isEmpty(self):
        return self.items == []

    # 将new加入栈
    def push(self, new):
        self.items.append(new)

    # 查看栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 查看栈的大小
    def size(self):
        return len(self.items)

    # 删除栈顶元素
    def pop(self):
        return self.items.pop()
