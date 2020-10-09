info_tuple = ("zhangsan", 18, 1.85)

# 1. 取值和取索引
print(info_tuple[0])
print(info_tuple.index(1.85))

# 2. 统计个数
print(info_tuple.count("zhangsan"))

print("%s的年龄是: %d, 身高是: %.1f米" % info_tuple)

for i in info_tuple:
    print(i)

