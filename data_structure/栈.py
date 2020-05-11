# -*- coding:UTF-8 -*-

class Stack():
    '''栈'''
    def __init__(self):
        self.__list = []


    def push(self,item):
        '''添加新元素'''
        self.__list.append(item)


    def pop(self):
        '''弹出元素'''
        self.__list.pop()


    def peek(self):
        '''返回栈顶元素'''
        return self.__list[-1] if self.__list else None


    def is_empty(self):
        '''判断是否为空'''
        return False if len(self.__list) else True
         

    def size(self):
        '''返回栈高度'''
        return len(self.__list)


def main(): 
    s = Stack()
    s.push(1)
    s.push(3)
    ss = s.is_empty()
    print(False == ss)
    print(s.size())


if __name__ == "__main__":
    main()