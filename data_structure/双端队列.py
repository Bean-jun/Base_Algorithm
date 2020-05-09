class Deque():
    '''双端队列'''
    def __init__(self):
        self.__list = []

    def add_front(self,item):
        '''在头部添加'''
        self.__list.append(item)
        
        
    def add_rear(self,item):
        '''在尾部添加'''
        self.__list.insert(0,item)
        
        
    def pop_front(self):
        '''在头部删除'''
        return self.__list.pop()
        

    def pop_rear(self):
        '''在尾部删除'''
        return self.__list.pop(0)


    def is_empty(self):
        '''判断是否为空'''
        return False if len(self.__list) else True

    
    def size(self):
        '''返回队列长度'''
        return len(self.__list)


def main(): 
    dq = Deque()
    dq.add_front(1)
    dq.add_front(3)
    dq.add_front(6)
    dq.add_rear(999)
    dq.add_rear(98)
    print(dq.pop_front())
    print(dq.pop_rear())
    qq = dq.is_empty()
    print(False == qq)
    print(dq.size())


if __name__ == "__main__":
    main()