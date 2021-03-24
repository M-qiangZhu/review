def list_sort():
    my_list = [6, 10, 3, 20, 15, 4]

    for i in range(len(my_list)):
        # 假定当前位置为最大值
        max_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] > my_list[max_index]:
                max_index = j
        # 将当前最大值保存到 i 处
        temp = my_list[i]
        my_list[i] = my_list[max_index]
        my_list[max_index] = temp

    print(f"排序结果: {my_list}")

if __name__ == '__main__':
    list_sort()





