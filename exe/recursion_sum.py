def test(sum):
    x = int(input("请输入x: "))
    if x == 0:
        sum = 0
    else:
        test(sum)
        sum += x
    print(sum)

test(2)

