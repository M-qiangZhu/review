class Cat:

    def eat(self):
        # self就是当前调用的方法的对象, 类似于java中的this
        print("%s猫 在吃鱼" % self.name)

    def drink(self):
        print("%s猫 在喝水" % self.name)


tom = Cat()

tom.eat()
tom.drink()

tom.name = "Tom"
