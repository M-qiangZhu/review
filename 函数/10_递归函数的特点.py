def sum_number(num):
    print(num)

    # 递归出口, 一般出现在递归调用语句前面
    if num == 1:
        return

    # 自己调用自己
    sum_number(num - 1)

sum_number(3)