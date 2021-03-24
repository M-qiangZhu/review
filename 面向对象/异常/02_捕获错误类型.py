try:
    num = int(input("输入一个整数: "))
    result = 10 / num
    print(result)
except ValueError:
    print("请输入正确的整数!")
except ZeroDivisionError:
    print("除0错误")
except Exception as result:
    print("未知错误 : %s" % result)

print("-" * 50)