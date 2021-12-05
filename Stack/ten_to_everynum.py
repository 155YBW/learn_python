# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/9 10:49
---------------------------------------------
"""
from Stack.definition import Stack

def divideBy2(dec_num, base):
    stack = Stack()
    num = '0123456789ABCDEF'

    while dec_num > 0:
        rem = dec_num % base
        stack.push(rem)
        dec_num = dec_num // base

    binString = ''
    while not stack.isEmpty():
        binString = binString + num[stack.pop()]

    return binString

if __name__ == '__main__':
    result = divideBy2(32,16)
    print(result)