# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/23 21:34
---------------------------------------------
"""
from LinkedList.unorderList import Node

class OrderList:
    '''
    采用链表实现有序表 \n
    Node定义不变 \n
    设置一个head保存链表表头 \n
    OrderedList()：创建一个新的空有序列表。它返回一个空有序列表并且不需要传递任何参数。\n
    add(item):在保持原有顺序的情况下向列表中添加一个新的元素，新的元素作为参数传递进函数而函数无返回值。假设列表中原先并不存在这个元素。\n
    remove(item):从列表中删除某个元素。欲删除的元素作为参数，并且会修改原列表。假设原列表中存在欲删除的元素。\n
    search(item)：在列表中搜索某个元素，被搜索元素作为参数，返回一个布尔值。\n
    isEmpty()：测试列表是否为空，不需要输入参数并且其返回一个布尔值。\n
    size()：返回列表中元素的数量。不需要参数，返回一个整数。\n
    index(item)：返回元素在列表中的位置。需要被搜索的元素作为参数输入，返回此元素的索引值。假设这个元素在列表中。\n
    pop()：删除并返回列表中的最后一项。不需要参数，返回删除的元素。假设列表中至少有一个元素。\n
    pop(pos)：删除并返回索引 pos 指定项。需要被删除元素的索引值作为参数，并且返回这个元素。假设该元素在列表中。\n
    '''
    def __init__(self):
        self.head = None

    def search(self, item):
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

    '''
    总结，链表的各种实现：
    1、首先在定义函数时，创建一个current来表示指向表头
    2、对于查找问题，在进入循环前，创建好决定状态的量（停止与否）
    3、在循环内实现current的指向变化，一些数据操作等
    '''

    def add(self, item):
        current = self.head
        previous = None
        stop = None
        while current != None and not stop:     #首先发现插入位置
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)                       #创建Node
        if previous is None:                    #判断是插入表头还是插入表中
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):
        current = self.head
        n = 0
        while current is not None:
            n = n + 1
            current = current.getNext()
        return n

    def isEmpty(self):
        return self.head == None

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

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    def pop(self):
        current = self.head
        previous = None                     #创建previous以获得最后一个NOde的前一个node
        while current.getNext() != None:    #判断下一个node是否存在
            previous = current              #获得最后一个NOde的前一个node
            current = current.next          #遍历整个表直到最后
        previous.setNext(current.getNext()) #将previous的next设为current的下一个，即删除current node
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
                current= current.getNext()
                n = n + 1
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        return current.getData()

guss = OrderList()
guss.add(10)
guss.add(1)
guss.add(21)
guss.add(18)
print(guss.search(10))
print(guss.search(4))
print(guss.isEmpty())
print(guss.index(18))
print(guss.size())
guss.remove(18)
print(guss.size())
print(guss.pop())
print(guss.size())
print(guss.pop_index(0))
print(guss.size())
