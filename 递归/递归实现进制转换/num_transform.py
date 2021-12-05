# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/12/5 10:55
---------------------------------------------
"""
# 输入默认为10进制
def num_tra(num, base):
    convString = "0123456789ABCDEF"
    if num < base:
        return convString[num]
    else:
        return num_tra(num//base, base) + convString[num % base]  # 字符串拼接

print(num_tra(2, 10))
print(type(num_tra(32, 16)))
