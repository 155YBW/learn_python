# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/5 11:00
---------------------------------------------
"""
# 逐个字符比较法 O(n^2)复杂度
def bwc(s1, s2):
    list2 = list(s2)  # 将s2字符串的字符，复制到列表之中
    pos1 = 0
    findOk = True  # 整体判断量，只要有一个字符未找到，就输出False
    while pos1 < len(s1) and findOk:  # 循环取出s1中每个字符
        pos2 = 0
        find = False
        while pos2 < len(list2) and not find:  # 循环与s2中的每个字符进行比较
            if s1[pos1] == list2[pos2]:
                find = True  # 单个字符判断量，找到变为Ture
            else:
                pos2 = pos2 + 1
        if find:
            list2[pos2] = None  # 找到后就打勾，防止下次重复判断
        else:
            findOk = False
        pos1 = pos1 + 1
    return findOk


if __name__ == '__main__':
    s1 = 'python'
    s2 = 'typhno'
    result = bwc(s1, s2)
    print(result)