name_list = ["zhangsan", "lisi", "wangwu"]

# 1. 取值和取索引
# list index out of range - 列表索引超出范围
print(name_list[2])

# 知道数据的内容, 想确定数据在列表中的位置
# print(name_list.index("zhangsan111"))  -- ValueError: 'zhangsan111' is not in list
print(name_list.index("zhangsan"))


# 2. 修改
name_list[1] = "李四"
# name_list[3] = "王小二" -- list assignment index out of range
# 列表索引超出范围, 报错

# 3. 增加
# append方法 向列表末尾追加数据
name_list.append("王小二")

# insert方法 向列表指定索引位置插入数据
name_list.insert(1, "插到索引为1处")

# extend方法 将另一个列表中的所有内容添加到当前列表的末尾
temp_list =["大佬", "大佬", "二老", "三老"]
name_list.extend(temp_list)


# 4. 删除
# pop方法 删除指定索引位置的数据
name_list.pop(-1)

# remove方法 删除指定内容的数据, 只会删除第一个数据, 如果数据不存在, 会报错
name_list.remove("二老")

# del关键字 本质上是用来将一个变量从内存中删除的, 一旦被删除, 后面的代码就无法在使用
# 提示: 在日常开发中,要从列表删除数据,建议使用列表提供的方法
del name_list[1]


# 5. 统计
# len()函数 统计列表中元素的总数
list_len = len(name_list)
print("列表中包含%d个元素" % list_len)

# count方法 统计某个数据在列表中出现的次数
count = name_list.count("大佬")
print("大佬出现了%d次" % count)

# 6. 循环遍历
# 使用迭代遍历列表
for my_name in name_list:
    print("我的名字叫%s" % my_name)

print(name_list)
