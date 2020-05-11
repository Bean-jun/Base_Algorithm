# -*- coding:UTF-8 -*-


# 单链表
class Node():
    '''创建单链表节点类'''
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList():
    '''定义单链表类'''
    def __init__(self):
        # 初始化链表指针和链表长度
        self.head = None
        self.length = 0
    
    def demo(self):
        '''演示'''
        node1 = None
        node2 = Node('hei', None)
        node3 = Node('ha', node2)
        print(node1, node2.data, node3.data, node3.next, node3.next.data)
    
    def createlinkedlist(self):
        '''创建单链表'''
        for count in [11, 14, 15, 22, 232]:
            self.head = Node(count, self.head)
            self.length += 1
        # print(self.head.data, self.length)
        return self.head,self.length # 返回链表和链表长度

    def printcreatelinkedlist(self):
        '''打印单链表'''
        head = self.head
        length = self.length
        node_list = []
        while length > 0:
            node_list.append(head.data)
            head = head.next
            length -= 1
        print(node_list)
    
    def traversal(self):
        '''链表的遍历'''
        head = None
        for count in range(10, 28, 5):
            head = Node(count, head)
        while head != None:
            print(head.data)
            head = head.next
    
    def searchtarget(self,target): 
        '''搜索链表中的某一个值'''
        temp = self.head
        print(type(temp))
        while temp.data != target and temp != None:
            # print(temp.data)
            temp = temp.next
            if temp == None:
                break
        if temp != None:
            print(str(target) + '已找到')
        else:
            print(str(target) + '不存在')

    def searchindex(self,index):
        '''访问链表的某一项'''
        head = self.head
        while index > 0:
            head = head.next
            index -= 1
        print(head.data)
    
    def replacetarget(self,target,new_target):
        '''链表对应元素值的替换'''
        head = self.head
        while head.data != target and head != None:
            head = head.next
            if head == None:
                break
        if head != None:
            head.data = new_target
            print('替换后值为'+ str(head.data))
        else:
            print('未找到'+str(target))
    
    def replaceindex(self,index,new_target):
        '''链表对应索引值的替换'''
        head = self.head
        while index > 0:
            head = head.next
            index -= 1
        head.data = new_target
        print('替换后'+ str(head.data))

    def inserttarget(self,target):
        '''在链表中插入新元素'''
        if self.head == None: # 不存在就创建一个
            self.head = Node(target, self.head)
        else: # 存在就在后面追加
            head = self.head
            while head.next != None:
                head = head.next
            head.next = Node(target,None)
        self.length += 1
    
    def insert_anywhere_target(self,index,target):
        '''在链表的任意位置插入新元素'''
        if self.head == None or index <= 0:
            self.head = Node(target,self.head)
        else:
            head = self.head
            while index >= 1 and head.next != None:
                head = head.next
                index -= 1
            head.next = Node(target,head.next)
        self.length += 1
    
    def deletetarget(self):
        '''删除掉末尾的链表值'''
        if self.head.next == None:
            self.head = None
        else:
            head = self.head
            while head.next != None:
                head = head.next
            head.next = None
        self.length -= 1
    
    def delete_index_target(self,index):
        '''删除链表任意位置的值'''
        if self.head.next == None or index <= 0:
            self.head = self.head.next
        else:
            head = self.head
            while head.next != None and index > 1:
                head = head.next
                index -= 1
            head.next = head.next.next
        self.length -= 1

if __name__ == '__main__':
    Li = LinkedList()
    Li.demo()
    Li.createlinkedlist()
    Li.printcreatelinkedlist()
    Li.traversal()
    Li.searchtarget(999)
    Li.searchindex(4)
    Li.replacetarget(22,999)
    Li.searchtarget(999)
    Li.replaceindex(4,666)
    Li.printcreatelinkedlist()
    Li.inserttarget(888)
    Li.printcreatelinkedlist()
    Li.insert_anywhere_target(0,520)
    Li.printcreatelinkedlist()
    Li.deletetarget()
    Li.printcreatelinkedlist()
    Li.delete_index_target(0)
    Li.printcreatelinkedlist()
