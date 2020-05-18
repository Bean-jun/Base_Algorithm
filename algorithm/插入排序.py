# -*- conding:UTF-8 -*-


def insert_sort(lists):
    '''插入排序'''
    for i in range(len(lists)-1):
        for j in range(i+1, 0, -1):
            if lists[j] < lists[j-1]:
                lists[j], lists[j-1] = lists[j-1], lists[j]
            else:
                break
    return lists


if __name__ == "__main__":
    from random import randint
    list01 = [randint(1, 10000) for i in range(5)]
    print('原列表：' + str(list01))
    # 开始排序
    list02 = insert_sort(list01)
    print('排序后：' + str(list02))