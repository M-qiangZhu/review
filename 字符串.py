# 通常用双引号定义字符串
str1 = "hello python"

# 如果字符串中有单引号, 则用单引号定义字符串
str2 = '我的外号是"大西瓜"'

print(str1)
print(str1[6])  # 用[]获取字符串的元素,索引从0开始
print(str2)

for char in str2:
    print(char)

"""
字符串常用操作
"""
# 1. 统计字符串长度 len()
print(len(str1))

# 2. 统计某个子字符串出现的次数 count()
print('子字符串"llo"出现的次数:', str1.count("llo"))
print('子字符串"abc"出现的次数:', str1.count("abc"))

# 3. 获得某个子字符串出现的位置 index()
# 如果传入的子字符串不在主字符串中,程序会报错
print('子字符串"llo"出现的位置:', str1.index("llo"))
# print("字符串'llo'出现的位置:", str1.index("abc"))

"""
判断类型方法
"""
# 1. 判断空白字符 string.isspace()
space_str1 = " "
space_str2 = "\t\r\n"
print("空字符:", space_str1.isspace())
print("换行, 回车, 制表符:", space_str2.isspace())

# 2. 判断字符串中是否只包含数字
num_str1 = "1"
num_str2 = "\u00b2"
num_str3 = "一千零一"
# 这三个方法都不能判断小数
# num_str = "1.1"
print(num_str1.isdecimal())  # 只能判断数字, 开发时绝大多数时候选择isdecimal()
print(num_str2.isdigit())  # 可以判断全角数字和Unicode字符串
print(num_str3.isnumeric())  # 判断全角数字和汉字数字

"""
文本对齐
"""
# 假设: 以下内容是从网络上爬取的
# 要求: 顺序并且居中对齐输出以下的内容
poem1 = [
    "登黄鹤楼",
    "王之涣",
    "白日依山尽",
    "黄河入海流",
    "欲穷千里目",
    "更上一层楼"
]

# 1. 居中对齐
for poem_str in poem1:
    print("|%s|" % poem_str.center(10, "　"))  # 默认用英文空格填充, 输入法切换到全角后,使用中文空格

# 2. 左对齐
for poem_str in poem1:
    print("|%s|" % poem_str.ljust(10, "　"))

# 2. 右对齐
for poem_str in poem1:
    print("|%s|" % poem_str.rjust(10, "　"))

"""
删除空白字符
"""
poem2 = [
    "\t\n登黄鹤楼",
    "王之涣",
    "白日依山尽\t\n",
    "黄河入海流",
    "欲穷千里目",
    "更上一层楼"
]

for poem_str in poem2:
    # 先使用strip方法去除字符串中的空白字符
    # 再使用center方法居中显示文本
    print("|%s|" % poem_str.strip().center(10, "　"))

"""
字符串的拆分和连接
"""
# 要求:
# 1. 将字符串中的空白字符全部去掉
# 2. 在使用"　"作为分隔符, 拼接成一个整齐的字符串
poem3 = "登黄鹤楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目 更上一层楼"

# 拆分字符串 split()
poem3_list = poem3.split()  # 默认以空白字符做分隔符, 结果为列表形式
print(poem3_list)  # ['登黄鹤楼', '王之涣', '白日依山尽', '黄河入海流', '欲穷千里目', '更上一层楼']

# 合并字符串 join(iterable)
result = "　".join(poem3_list)  # 以"　"为间隔符,插入到以poem3_list迭代出来的所有字符串之间
print(result)  # 登黄鹤楼　王之涣　白日依山尽　黄河入海流　欲穷千里目　更上一层楼


"""
字符串的切片
"""



