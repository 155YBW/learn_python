# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/12/12 10:57
---------------------------------------------
比较难多理解
"""
# 逻辑：h代表盘子的大小，从f位置经过w位置移动到t位置
def moveTower(h, f, w, t):
    if h >= 1:
        moveTower(h-1, f, t, w)
        moveDisk(h, f, t)
        moveTower(h-1, w, f, t)

def moveDisk(disk, f, t):
    print(f'Moving disk[{disk}] from {f} to {t}')

moveTower(3, '-1-', '-2-', '-3-')
