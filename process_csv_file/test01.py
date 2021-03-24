import pandas as pd

time_dt = pd.read_csv('run_times.csv', header=None)  # 读取csv文件, 列名为空
conts_dt = pd.read_csv('result_conts.csv', header=None)
# print(time_dt)

# print(time_dt.shape)  # shape[0]表示行数, shape[1] 表示列数

# 获取 run_times 行数
time_dt_lines = time_dt.shape[0]
conts_dt_lines = conts_dt.shape[0]

if time_dt_lines == conts_dt_lines:
    lines = time_dt_lines
    for i in range(int(lines / 4)):
        # 每次向后读取四行
        sub_time_dt = pd.read_csv('run_times.csv', skiprows=i * 4, nrows=4, header=None)
        sub_cnots_dt = pd.read_csv('result_conts.csv', skiprows=i * 4, nrows=4, header=None)
        # 设置列名
        sub_time_dt.columns = ['times', 'pid', 'type']
        sub_cnots_dt.columns = ['gates', 'pid']
        # 合并两个文件
        sub_dt = pd.merge(sub_cnots_dt, sub_time_dt, on=['pid'], how='inner')
        print(sub_dt)
        # 获取当前times列最小值
        

        # print(sub_time_dt)
        # print(sub_cnots_dt)
        print("-" * 50)
else:
    print("数据行数不匹配!!!")



# print(time_dt)



