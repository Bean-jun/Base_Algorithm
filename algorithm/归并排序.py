# -*- coding:UTF-8 -*-


def merge_sort(lists):
    '''归并排序'''
    if len(lists) <= 1:
        return lists

    # 使用递归的方式进行切分,并讲切分的数据进行排序后合并
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])

    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)
    return merged


if __name__ == "__main__":
    from random import randint
    list01 = [randint(1, 10000) for i in range(5)]
    print('原列表：' + str(list01))
    # 开始排序
    list02 = merge_sort(list01)
    print('排序后：' + str(list02))