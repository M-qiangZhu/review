# 全局变量
num = 10

def demo1():
    num = 100
    print("demo1 ==> %d" % num)  # 先在函数内部查找


def demo2():
    print("demo2 ==> %d" % num)

demo1()
demo2()