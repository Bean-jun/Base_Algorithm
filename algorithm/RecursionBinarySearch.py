def recursion_binary_search(lists, left_number, right_number, number):
    '''递归二分法查找搜索'''

    middle_number = (left_number + right_number) // 2
    if number == lists[middle_number]:
        way = middle_number + 1
        print('该数所在列表位置是：' + str(way))

    elif number > lists[middle_number]:

        return recursion_binary_search(lists, middle_number, right_number, number)
    else:

        return recursion_binary_search(lists, left_number, middle_number, number)

if __name__ == "__main__":
    '''测试查找'''
    list01 = [i for i in range(100)]
    print('原列表：' + str(list01))
    # 开始查找
    recursion_binary_search(list01, list01[0], list01[-1], 35)