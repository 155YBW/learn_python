# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/9 10:01
---------------------------------------------
"""
from definition import Stack

def parChecker(symbolString):
    s = Stack()
    balance = True
    index = 0
    if len(symbolString) == 0:  # 空字符串不算
        balance = False
        print('字符串为空')
    while index < len(symbolString) and balance:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balance = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balance = False
        index = index + 1
    if s.isEmpty() and balance:
        print(True)
    else:
        print(False)


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.find(open) == closers.find(close)

if __name__ == '__main__':
    parChecker('((([[]])))')
    parChecker('()(()())')
    parChecker('((()')
    parChecker('{[]}')