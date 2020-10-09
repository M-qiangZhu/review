import random

num = random.randint(1, 2)

age = int(input("请输入年龄: "))

if age >= 18:

    # 成年
    print("已经成年")
    print(num)

else:
    # 未成年
    print("对不起,还未成年^_^")
