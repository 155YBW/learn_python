# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/5 11:44
---------------------------------------------
"""
# 计数比较法 O(n) 牺牲存储空间换取运行速度 要注意权衡存储空间与运行时间
def bwc(s1, s2):
    list1 = [0 for i in range(0, 26)]
    list2 = [0]*26
    print(list1)
    print(list2)
    for i in range(len(s1)):
        list1[ord(s1[i])-97] = list1[ord(s1[i])-97] + 1
    for i in range(len(s2)):
        list2[ord(s2[i])-97] = list2[ord(s2[i])-97] + 1
    print(list1)
    print(list2)
    if list1 == list2:
        reslt = True
    else:
        reslt = False
    return reslt

if __name__ == '__main__':
    s1 = 'python'
    s2 = 'typhnn'
    reslt = bwc(s1, s2)
    print(reslt)