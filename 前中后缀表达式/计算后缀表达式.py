# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/12 14:14
---------------------------------------------
"""
from Stack.definition import Stack


def postfixEval(postfixExpr):
    nums = "0123456789"
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in nums:
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            if result == str("error"):
                print("计算符号输入有误")
                break
            else:
                operandStack.push(result)
    if operandStack.size() == 1:
        return operandStack.pop()
    else:
        return str("error")


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    else:
        return str("error")