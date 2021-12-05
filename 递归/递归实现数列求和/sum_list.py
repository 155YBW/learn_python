# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/12/5 10:29
---------------------------------------------
"""
def sum_list(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + sum_list(numList[1:])


print(sum_list(list([1, 3, 5, 7, 9])))
