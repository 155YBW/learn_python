# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/12 10:38
---------------------------------------------
前后缀方法思路：
运算符 变量1 变量2
例如： +AB --> A+B
     +A*BC --> B*C+A
算法思路（以前缀为例）
(A+(B*C)) ---> +A*BC
将操作符号移动到最近的左括号处，并删除右括号就得到了前缀表达式。
"""
from Stack.definition import Stack


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
    test_1 = "( A + ( B * C ) )"
    out_test_1 = infixToPostfix(test_1)
    print(out_test_1)