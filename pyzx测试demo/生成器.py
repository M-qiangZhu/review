def steiner_g():
    i = 10
    print(i)
    while i < 20:
        print("生成器执行前...")
        yield i+1
        print("生成器执行后...")
        i += 1
    print("循环结束")
