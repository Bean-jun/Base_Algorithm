def binary_search(lists, number):
    '''二分查找搜索'''
    left_number = 0
    right_number = len(lists)

    while left_number < right_number:
        middle_number = (left_number + right_number) // 2
        if number == lists[middle_number]:
            way = middle_number + 1
            print('该数所在列表位置是：' + str(way))
            break
        elif number > lists[middle_number]:
            left_number = middle_number

        else:
            right_number = middle_number


if __name__ == "__main__":
    '''测试查找'''
    list01 = [i for i in range(100)]
    print('原列表：' + str(list01))
    # 开始查找
    binary_search(list01, 35)
    