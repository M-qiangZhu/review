def demo(num, *args, **kwargs):

    print(num)
    print(args)
    print(kwargs)


print("======传一个参数======")
demo(1)
print("======传多个参数======")
demo(1, 2, 3)
demo(1, 2, 3, 4, 5)
print("======传键值对参数======")
demo(1, 2, 3, 4, 5, name="小明")
demo(1, 2, 3, 4, 5, name="小明", age=18)
