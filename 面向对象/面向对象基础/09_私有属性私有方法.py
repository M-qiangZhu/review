class Women:

    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象方法内部,可以访问对象的私有属性
        print("%s 的年龄是 %d" % (self.name, self.__age))

xf = Women("小芳")

# 私有属性,在外界不能被直接访问
print(xf._Women__age)


# 私有方法,不允许在外界直接访问
xf._Women__secret()