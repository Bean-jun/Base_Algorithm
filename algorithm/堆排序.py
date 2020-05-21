# -*- coding:UTF-8 -*-


def head_sort(lists):
    '''堆排序'''
    temp_list = [0]
    temp_list.extend(lists)
    val = []
    while len(temp_list) > 1:
        # 使用数列建立最小堆，每次取出最小元素，并重新建堆
        temp_list = _bulid_heap(temp_list)
        val.append(temp_list.pop(1))
    return val

def _bulid_heap(*args):
    '''将元素组合为最小堆形式，并返回'''
    lists = list(*args)
    temp = len(lists) - 1
    # 交换元素，实现最小堆
    while temp:
        num = temp
        while num > 1:
            index = num // 2
            if lists[num] < lists[index]:
                lists[num], lists[index] = lists[index], lists[num]
            num = index
        temp -= 1
    return lists


if __name__ == "__main__":
    from random import randint
    list01 = [randint(1, 10000) for i in range(5)]
    print('原列表：' + str(list01))
    # 开始排序
    list02 = head_sort(list01)
    print('排序后：' + str(list02))