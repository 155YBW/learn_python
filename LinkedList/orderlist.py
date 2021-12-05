# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/23 20:14
---------------------------------------------
"""
from LinkedList.unorderList import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        """
        思路： 由于是有序表，需要在合适的位置插入，即大于前一项，小于后一项。
        :param item: 需要添加的数据项
        :return: None
        """
        current = self.head
        previous = None  # 存储前一项指向
        stop = False
        # 寻找插入位置
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                current = current.getNext()

        temp = Node(item)  # 创建节点类
        # 表头插入
        if previous == None:
            temp.setNext(self.head)  # head的指向改成temp指向
            self.head = temp  # head指向temp
        # 表中/尾插入
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def remove(self, item):
        current = self.head
        previous = None  # 保存需要删除节点的上一个节点的信息，删除节点就相当于指针绕过这个节点
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        # 分两个情况，第一个是特殊情况，即要删除第一个节点，直接head绕过第一个节点即可
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def search(self, item):
        """
        思路： 以数值为例，由于是有序表，查找元素从第一项开始比较，
        若小于item，则继续查找，若大于item，则结束查找。
        :param item: 需要寻找的数据项
        :return: found: 是否找到item
        """
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found


    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count


    # 网上的
    def popLast(self):
        current = self.head
        previous = None  # 创建previous以获得最后一个NOde的前一个node
        while current.getNext() != None:  # 判断下一个node是否存在
            previous = current  # 获得最后一个NOde的前一个node
            current = current.next  # 遍历整个表直到最后
        previous.setNext(current.getNext())  # 将previous的next设为current的下一个，即删除current node
        return current.getData()

    def pop_index(self, pop):
        current = self.head
        previous = None
        found = False
        n = 0
        while current != None and not found:
            if n == pop:
                found = True
            else:
                previous = current
                current = current.getNext()
                n = n + 1
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        return current.getData()

    def index(self, item):
        current = self.head
        found = False
        n = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                n = n + 1
        return n






