def print_line(char, times):
    """打印单行分隔线

    :param char: 分隔线使用的字符
    :param times: 字符重复次数
    """
    print(char * times)


def print_lines(char, times, rows):
    """打印多行分隔线

    :param char: 分隔线使用的字符
    :param times: 字符重复次数
    :param rows: 打印行数
    """
    i = 0
    while i < rows:
        print_line(char, times)
        i += 1


name = "测试模块"
