# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/20 11:16
---------------------------------------------
链表从第一个元素head开始，到最后一个元素结束end
初始应默认设置表头head指向为None
数据都存储在节点中
"""
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

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

    # 函数待完善

