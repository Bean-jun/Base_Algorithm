# -*- coding:UTF-8 -*-


def quick_sort(lists,left,right):
    '''快速排序'''

    # 递归结束条件
    if left > right:
        return 

    base_num = lists[right]
    start = left
    end = right

    while start < end:
        # 前游标
        while start < end and lists[start] <= base_num:
            start += 1

        # 后游标
        while start < end and lists[end] >= base_num:
            end -= 1

        # 交换游标指向的元素
        lists[start], lists[end] = lists[end], lists[start]

        # 若是游标指向同一元素地址，则讲该元素和最后面的一个元素
        if start == end:
            lists[end], lists[right] = lists[right], lists[end]
    # 左边递归
    quick_sort(lists, left, start-1)
    
    # 右边递归
    quick_sort(lists, start+1, right)


if __name__ == "__main__":
    from random import randint
    list01 = [randint(1, 10000) for i in range(5)]
    print('原列表：' + str(list01))
    # 开始排序
    quick_sort(list01, 0, len(list01)-1)
    print('排序后：' + str(list01))