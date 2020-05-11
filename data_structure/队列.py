# -*- coding:UTF-8 -*-

class Queue():
    '''队列'''
    def __init__(self):
        self.__list = []
    
    def enqueue(self, item):
        '''在队列中添加元素'''
        self.__list.append(item)


    def dequeue(self):
        '''从头部删除一个元素'''
        return self.__list.pop(0)


    def is_empty(self):
        '''判断是否为空'''
        return False if len(self.__list) else True


    def size(self):
        '''返回队列长度'''
        return len(self.__list)


def main(): 
    q = Queue()
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(6)
    print(q.dequeue())
    qq = q.is_empty()
    print(False == qq)
    print(q.size())


if __name__ == "__main__":
    main()