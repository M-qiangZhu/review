# 导入工具包
import keyword

# 单行注释
print("test")

print(1 + 2 * 3)  # 输出表达式结果

"""
多行注释
......
......
多行注释结束了
"""

# 1. 定义一个变量记录 QQ 号码
qq_number = "1234567"

# 2. 定义一个变量记录 QQ 密码
qq_password = 123

print("qq_number = " + qq_number)
print(qq_password)

name = "小明"
age = 18
gender = True
height = 1.75
weight = 75.0

# price = float(input("输入单价: "))
# weight = float(input("输入重量: "))

student_no = 123

# print("单价是%.02f, 重量是%.01f" % (price, weight))
print("我的学号是%06d" % student_no)

print(keyword.kwlist)
