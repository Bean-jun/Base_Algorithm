# -*- coding:UTF-8 -*-


def shell_sort(lists):
    '''希尔排序'''
    sublistcount = len(lists) // 2
    while sublistcount > 0:
        for i in range(sublistcount):
            gap_insert_sort(lists, i, sublistcount)
        sublistcount //= 2
    return lists

def gap_insert_sort(lists,start,gap):
    for i in range(start,len(lists)-1, gap):
        for j in range(i+1,0,-gap):
            if lists[j] < lists[j-gap]:
                lists[j], lists[j-gap] = lists[j-gap], lists[j]
            else:
                break


if __name__ == "__main__":
    from random import randint
    list01 = [randint(1, 10000) for i in range(5)]
    print('原列表：' + str(list01))
    # 开始排序
    list02 = shell_sort(list01)
    print('排序后：' + str(list02))