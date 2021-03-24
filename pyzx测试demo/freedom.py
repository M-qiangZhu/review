import numpy as np


def is_in_grid(x, y, n, m):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    else:
        return True


def generate_list(n, m):
    a = []
    for i in range(n):
        a.append([])
        for j in range(m):
            a[i].append(1)
    return a


def freedom(n, m):
    step = [[-1, 0],
            [1, 0],
            [0, -1],
            [0, 1]]
    list = generate_list(n, m)
    for i in range(n):
        for j in range(m):
            for k in range(len(step)):
                x = i + step[k][0]
                y = j + step[k][1]
                if is_in_grid(x, y, n, m):
                    list[i][j] = list[i][j] + 1
    new_list = (np.array(list) - 1).tolist()
    return new_list


print(freedom(3, 4))



