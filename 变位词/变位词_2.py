# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/5 11:24
---------------------------------------------
"""
# 排序比较法 O(n*logn)复杂度
def bwc(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    list1.sort()  # 排序算法存在复杂度的增加
    list2.sort()
    sum1 = 0
    sum2 = 0
    i = 0
    same = True
    while i < len(list1) and same:
        sum1 = sum1 + ord(list1[i])
        sum2 = sum2 + ord(list2[i])
        if sum1 == sum2:
            i = i + 1
        else:
            same = False
    return same, sum1, sum2

if __name__ == '__main__':
    s1 = 'python'
    s2 = 'typhno'
    reslt, sum1, sum2 = bwc(s1, s2)
    print(sum1)
    print(sum2)
    print(reslt)