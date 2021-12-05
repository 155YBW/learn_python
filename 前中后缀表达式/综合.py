# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/12 14:23
---------------------------------------------
"""
from Stack.definition import Stack


# 计算后缀表达式
def postfixEval(postfixExpr):
    nums = "0123456789"
    norm = True
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        # 如果是数字就放入栈
        if token in nums:
            operandStack.push(int(token))
        # 如果是符号就开始计算，顺序是：第二次取出元素 运算符 第一次取出的元素
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            if result == str("error"):
                print("计算符号输入有误")
                norm = False
                break
            else:
                operandStack.push(result)
    if operandStack.size() == 1 and norm:
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


# 定义中缀转后缀函数
def infixToPostfix(infixexpr):
    # 定义字符表
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "0123456789"
    # 记录符号优先级
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1  # 左括号不参与交换输出，用于与右括号抵消
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()  # 解析输入的中缀表达式

    for token in tokenList:
        # 如果是计算变量直接加入列表
        if token in letters or token in nums:
            postfixList.append(token)
        # 如果是左括号则压入栈中
        elif token == "(":
            opStack.push(token)
        # 遇到右括号则开始从栈中输出
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        # 遇到符号则比较优先级，将高优先级的输出，低的压入栈
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())  # 栈顶元素若为高优先级则取出并加入列表
            opStack.push(token)  # 将符号放入栈中

    # 将转换结果输出
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return "".join(postfixList)

if __name__ == '__main__':
    test_1 = "( 5 + ( 9 * 6 ) )"
    test_2 = "5 9 6 / +"
    out_test_1 = infixToPostfix(test_1)
    print(out_test_1)
    num_test_2 = postfixEval(test_2)
    print(num_test_2)