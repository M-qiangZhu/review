def measure():
    """测量温度和湿度"""

    print("开始测量...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 如果函数返回的类型时元组,可以省略小括号
    # return (temp, wetness)
    return temp, wetness


# 需要单独处理温度和湿度
# 如果在开发中, 函数返回的类型时是元组, 希望同时单独处理元祖中的元素
# 可以使用多个变量,一次性接收函数的返回结果
# 注意: 使用多个变量接收结果时, 变量的个数应该和元组中的个数保持一致
gl_temp, gl_wetness = measure()

print(gl_temp)
print(gl_wetness)