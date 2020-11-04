# 全局变量
num = 10

def demo1():

    # 希望在函数内部修改全局变量的值 -- 使用global声明变量
    # global关键字会告诉解释器后面的变量是一个全局变量
    # 在函数内部使用赋值语句时,就不会创建局部变量了
    global num
    num = 100
    print("demo1 ==> %d" % num)  # 先在函数内部查找


def demo2():
    print("demo2 ==> %d" % num)

demo1()
demo2()