# -*- conding:UTF-8 -*-


def select_sort(lists):
    '''选择排序'''
    for i in range(len(lists)-1):
        # 建立起始下标开始遍历，利用range的特性，依次开始遍历每一个下标
        min_index = i
        for j in range(i+1, len(lists)):
            # 针对元素进行遍历，与第一个元素相比较，将最小元素索引保留并返回
            if lists[j] < lists[min_index]:
                min_index = j
        if min_index != i:
            # 判断最小索引是否应该在合适位置，不在，则进行交换
            lists[i], lists[min_index] = lists[min_index], lists[i]
    return lists
    


if __name__ == "__main__":
    from random import randint
    list01 = [randint(1, 10000) for i in range(5)]
    print('原列表：' + str(list01))
    # 开始排序
    list02 = select_sort(list01)
    print('排序后：' + str(list02))