# 创建类
class Cat:
    def eat(self):
        print("猫吃鱼")
    def drink(self):
        print("猫喝水")


# 创建对象, 对象内存地址不同
tom = Cat()
tom.name = "汤姆"


# 调用方法
tom.eat()
tom.drink()
print(tom.name)

print(tom)
addr = id(tom)
print("%d" % addr)
print("%x" % addr)
