# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/19 10:56
---------------------------------------------
"""
from Queue_test.Deque import deque


def palcjecker(aString):
    chardeque = deque()

    for ch in aString:
        chardeque.addRear(ch)
    # # 写法1
    # hwc = True
    # for i in range(chardeque.size()//2):
    #     ch_rear = chardeque.removeRear()
    #     ch_front = chardeque.removeFront()
    #     if ch_front != ch_rear:
    #         hwc = False
    #         break
    #
    # if hwc:
    #     return True
    # else:
    #     return False

    # 写法2
    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

if __name__ == '__main__':
    print(palcjecker("abcbaablcba"))