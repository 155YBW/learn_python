# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/16 15:19
---------------------------------------------
1.打印排队的容量有多大？
2.不同的打印模式消耗的时间不一样。
实例：
1.确认生成概率
每小时10个学生提交20个作业
概率是没3min（180s）会有一个作业生成并提交
则概率是每秒1/180
2.确定打印页数
每个任务是1-20页，概率相同

模拟流程：
1 创建打印队列对象
2 计时
    按照概率生成打印作业，加入打印队列
    如果打印机空闲且队列不为空，则取出队首作业打印，记录作业等待时间
    如果打印机忙，按照打印速度1s打印
    如果当前任务打印完成，则打印机进入空闲
3 完毕，统计平均等待时间
"""
from Queue_test.def_Queue import Queue
import random


class Printer:
    # 初始化
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印速度为ppm，每分钟打印几页
        self.currentTask = None  # 打印任务
        self.timeRemaining = 0  # 打印任务倒计时

    # 打印工作函数
    def tick(self):
        if self.currentTask != None:  # 如果存在打印任务（打印机忙），则打印
            self.timeRemaining = self.timeRemaining - 1  # 每次打印耗时1s
            if self.timeRemaining <= 0:  # 如果打印完成
                self.currentTask = None  # 接触忙状态

    # 查忙函数
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    # 分配打印任务函数
    def startNext(self, newtask):
        self.currentTask = newtask  # 设置新任务
        self.timeRemaining = newtask.getPages()/self.pagerate*60  # 计算打印所需时间


class Task:
    # 初始化
    def __init__(self, time):
        self.timestamp = time  # 生成时间戳
        self.pages = random.randrange(1, 21)  # 打印页数在1-20页随机

    # 记录时间函数
    def getStamp(self):
        return self.timestamp  # 获取当前时间

    # 获取打印页数
    def getPages(self):
        return self.pages  # 获取打印页数

    # 计算等待时间函数
    def waitTime(self, currenttime):
        return currenttime - self.timestamp  # 计算等待时间


# 模拟任务发布函数
def newPrintTask():
    num = random.randrange(1, 181)  # 1/180的概率生成作业
    if num == 180:
        return True
    else:
        return False


def currentSecond(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)  # 赋值打印速度，同时生成Printer实例
    printQueue = Queue()  # 创建打印队列
    waitingtimes = []

    for currentSecond in range(numSeconds):  # 模拟时间流逝
        # 随机生成作业任务
        if newPrintTask():
            task = Task(currentSecond)  # 在此时刻生成任务
            printQueue.enqueue(task)  # 加入队列

        # 判断是否满足打印任务的条件
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()  # 退出队列，开始处理此任务
            waitingtimes.append(nexttask.waitTime(currentSecond))  # 计算处理时，等待时间
            labprinter.startNext(nexttask)

        labprinter.tick()  # 每次循环都工作一次，相当于每个时刻的工作

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f s, %3d tasks remaining." % (averageWait, printQueue.size()))


if __name__ == '__main__':
    for i in range(10):
        currentSecond(3600, 10)
