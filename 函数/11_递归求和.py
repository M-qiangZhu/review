def sum_nums(num):

    # 1. 出口
    if num == 1:
        return 1

    # 2. 记录前n-1个累加结果
    temp = sum_nums(num - 1)

    # 3. 返回最终结果
    return num + temp


print(sum_nums(100))