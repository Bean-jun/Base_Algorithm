# _*_ conding: UTF-8 _*_


# 单链表
class Node():
    '''创建单链表节点类'''
    def __init__(self,data,next=None):
        self.data = data
        self.next = None

class SinCycLinkedList():
    '''定义单项循环链表'''
    def __init__(self):
        # 初始化链表指针
        self.__head = None
    
    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head == None
    
    def length(self):
        '''获取链表长度'''
        num = 0
        cur = self.__head
        while cur != None and cur.next != self.__head:
            cur = cur.next
            num += 1
        return num

    def traversal(self):
        '''遍历链表'''
        if self.is_empty():
            return False
        cur = self.__head
        print(cur.data)
        # 由于是循环链表此处为判断链表尾部是否不等于头部
        while cur.next != self.__head:
            cur = cur.next
            print(cur.data)
    
    def add(self,data):
        '''在头部或者尾部添加节点'''
        node = Node(data)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            # 若链表存在，则移动到链表的尾部，直接插入
            cur  = self.__head
            while cur != None and cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
    
    def insert(self,index,data):
        '''在指定位置插入元素'''
        if index <= 0:
            self.add(data)
        else:
            cur = self.__head
            while cur.next != self.__head and index > 1:
                cur = cur.next
                index -= 1
            node = Node(data)
            node.next = cur.next
            cur.next = node
    
    def search(self,data):
        '''查找元素是否存在'''
        if self.is_empty():
            return False
        cur = self.__head
        if cur.data == data:
            return True
        while cur.next != self.__head:
            cur = cur.next
            if cur.data == data:
                return True
        return False

if __name__ == "__main__":
    Li = SinCycLinkedList()
    print(Li.is_empty())
    Li.add(2)
    Li.add(3)
    Li.add(4)
    Li.insert(1,23)
    Li.insert(2,23)
    print(Li.traversal())
    print('长度%d'%Li.length())
    print(Li.is_empty())
    print(Li.search(222))