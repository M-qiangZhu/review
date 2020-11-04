gl_num_list = [6, 3, 9]

# 不指定reserve参数时, 默认是升序排序, reserve就是缺省参数,默认值为False
gl_num_list.sort()
print(gl_num_list)

# 指定reserve参数为True,进行降序排序
gl_num_list.sort(reverse=True)
print(gl_num_list)
