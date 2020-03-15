def bubble_sort(lists):
    '''冒泡排序'''

    list_min = 0
    list_max = len(lists)
    while list_min < list_max:
        '''控制多次循环'''
        
        list_point = 1  # 内循环取得最大值游标
        while list_point < list_max - list_min:  # 判断游标的范围并将排出最大值弹出
            '''取列表最大值放在最后'''

            if lists[list_point - 1] > lists[list_point]:
                lists[list_point - 1], lists[list_point] = lists[list_point], lists[list_point - 1]  # 交换

            list_point += 1  # 游标向右移动

        list_min += 1

    return lists

if __name__ == "__main__":
    '''测试排序'''
    from random import randint
    list01 = [randint(1, 10000) for i in range(40)]
    print('原列表：' + str(list01))
    # 开始排序
    list02 = bubble_sort(list01)
    print('排序后' + str(list02))