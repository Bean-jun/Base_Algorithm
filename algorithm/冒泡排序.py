# -*- conding:UTF-8 -*-


def bubble_sort(lists):
    '''冒泡排序'''
    for i in range(len(lists)-1, 0, -1):
        # 每次循环会得到最大的，使用range(len(lists)-1, 0, -1)，则是模拟剪掉最大元素位置
        for j in range(i):
            # 按照顺序开始进行比较，将最大元素移送到最后
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
    return lists


if __name__ == "__main__":
    from random import randint
    list01 = [randint(1, 10000) for i in range(5)]
    print('原列表：' + str(list01))
    # 开始排序
    list02 = bubble_sort(list01)
    print('排序后：' + str(list02))