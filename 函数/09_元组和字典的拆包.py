def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_num = (1, 2, 3)
gl_dict = {"name": "小米", "age": 18}
demo(gl_num, gl_dict)
# 拆包
demo(*gl_num, **gl_dict)  # 等价于 demo(1, 2, 3, name="小明", age=18)
