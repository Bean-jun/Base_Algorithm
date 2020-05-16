# -*- coding:UTF-8 -*-


class MaxHeap():
    '''最大堆的实现'''
    def __init__(self):
        '''初始化-使用列表实现'''
        self.heaplist = [0]
        self.heaphigh = 0

    def insert(self,data):
        '''插入元素'''
        self.heaplist.append(data)
        self._dataUp()
        self.heaphigh += 1
        print(self.heaplist, self.heaphigh)

    def _dataUp(self):
        '''插入元素-上浮操作'''
        high = len(self.heaplist)-1
        while high > 1 :
            index = high // 2
            if self.heaplist[high] > self.heaplist[index]:
                self.heaplist[high],self.heaplist[index] = self.heaplist[index], self.heaplist[high]
            high = index
        return self.heaplist
    
    def del_max(self):
        '''删除最大值'''
        self._dataDown()
        self.heaplist.pop()
        self.heaphigh -= 1
        print(self.heaplist,self.heaphigh)

    def _dataDown(self):
        '''删除元素-下沉操作'''
        index = 1
        high = len(self.heaplist)
        data = self.heaplist[-1]
        while 2*index+1 < high:
            if self.heaplist[2*index] > self.heaplist[2*index+1]:
                if self.heaplist[2*index] > data:
                    self.heaplist[index],self.heaplist[2*index] = self.heaplist[2*index],data
                    index *= 2
                else:
                    return self.heaplist
            else:
                if self.heaplist[2*index+1] > data:
                    self.heaplist[index],self.heaplist[2*index+1] = self.heaplist[2*index+1],data
                    index = 2*index+1
                else:
                    return self.heaplist

    @property
    def find_max(self):
        '''返回最大元素'''
        return None if self.heaphigh == 0 else self.heaplist[1]

    @property
    def is_empty(self):
        return True if self.heaphigh == 0 else False

    @property
    def size(self):
        '''返回长度'''
        return None if self.heaphigh == 0 else self.heaphigh


if __name__ == '__main__':
    heap = MaxHeap()
    heap.insert(100)
    heap.insert(90)
    heap.insert(85)
    heap.insert(80)
    heap.insert(30)
    heap.insert(60)
    heap.insert(50)
    heap.insert(55)
    heap.insert(1010)
    heap.insert(10000)
    heap.insert(1)
    print(heap.find_max)
    print(heap.is_empty)
    print(heap.size)
    heap.del_max()
    heap.del_max()
    heap.del_max()
    heap.del_max()
    heap.del_max()
    heap.del_max()
    print(heap.find_max)
    print(heap.is_empty)
    print(heap.size)

