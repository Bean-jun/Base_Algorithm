# -*- coding:UTF-8 -*-


class Node():
    def __init__(self,data,prev=None,next=None):
        '''创建双链表节点'''
        self.data = data
        self.prev = prev
        self.next = next

class DLinkedList():
    '''双向链表'''
    def __init__(self):
        self.__head = None

    def is_empty(self):
        '''判断是否为空'''
        return self.__head == None
    
    def length(self):
        '''获取链表长度'''
        num = 0
        cur = self.__head
        while cur != None:
            cur = cur.next
            num += 1
        return num
    
    def traversal(self):
        '''遍历链表'''
        if self.is_empty():
            return False
        cur = self.__head
        while cur != None:
            print(cur.data)
            cur = cur.next

    def add(self,data):
        '''在头部插入元素'''
        node = Node(data)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def append(self,data):
        '''在尾部插入元素'''
        node = Node(data)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur
    
    def search(self,data):
        '''查找元素'''
        if self.is_empty():
            return False
        else:
            cur = self.__head
            while cur != None:
                if cur.data == data:
                    return True
                cur = cur.next
            return False
    
    def insert(self,index,data):
        '''在指定位置添加元素'''
        if index <=0:
            self.add(data)
        else:
            cur = self.__head
            while cur.next != None and index >1:
                cur = cur.next
                index -= 1
            node = Node(data)
            node.next = cur.next
            cur.next.prev = node
            cur.next = node
            node.prev = cur
        
    def remove(self,data):
        '''删除元素'''
        if self.is_empty():
            print('链表为空，无法删除')
        else:
            cur = self.__head
            if cur.data == data:
                if cur.next == None:
                    self.__head =None
                else:
                    cur.next.prev = None
                    self.__head = cur.next
                return data
            while cur.next != None and cur.next.next != None:
                if cur.data == data:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    return data
                cur = cur.next
            

if __name__ == "__main__":
    Li = DLinkedList()
    print(Li.is_empty())
    Li.add(2)
    Li.add(3)
    Li.add(4)
    Li.insert(1,23)
    Li.insert(2,25)
    # print(Li.traversal())
    # print('长度%d'%Li.length())
    # print(Li.is_empty())
    print(Li.search(23))
    print(Li.remove(4))
    print('长度%d'%Li.length())
    print(Li.is_empty())
    print(Li.traversal())
    print(Li.search(23))