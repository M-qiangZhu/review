"""
完整for循环
"""
num_list = [1, 2, 3, 4]
for i in num_list:
    if i == 4:
        break
    print(i)
else:
    print("循环体内的代码被完整执行")

print("循环结束")
