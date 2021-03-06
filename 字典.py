import pandas

xiaoming_dict = {"name": "小明",
                 "age": 18,
                 "gender": True}

# 使用print函数输出字典时, 输出的顺序和定义的顺序不一定一致,因为字典是一个无序的数据集合
print(xiaoming_dict)  # {'name': '小明', 'age': 18, 'gender': True}
print(xiaoming_dict["name"])
print(xiaoming_dict.get("name"))

# 1. 统计键值对数量
print(len(xiaoming_dict))

# 2. 合并字典
temp_dict = {"height": 1.75,
             "age": 20}
xiaoming_dict.update(temp_dict)

# 注意: 如果被合并的字典中包含已经存在的键值对, 会覆盖原有的键值对
print(xiaoming_dict)  # {'name': '小明', 'age': 20, 'gender': True, 'height': 1.75}

# 3. 清空字典
xiaoming_dict.clear()

# 4. 添加新的键值对(方法一)
# 如果字典中没有key,就会添加该键值对,如果已经有key了,就会覆盖对应的value值
xiaoming_dict["class"] = 1
xiaoming_dict["class"] = 2


# 4. 添加新的键值对(方法二)
# xiaoming_dict.fromkeys("scores", 100)


print(xiaoming_dict)



