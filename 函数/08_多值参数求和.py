def sum_numbers(*args):
    num = 0

    for i in args:
        num += i

    return num


result = sum_numbers(1, 2, 3, 4, 5)
print(result)