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
else:
    # 没有异常时才会执行的代码
    print("try中代码没有错误")
finally:
    #
    print("无论出现什么,都会执行!!!")

print("-" * 50)