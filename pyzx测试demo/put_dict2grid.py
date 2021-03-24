dict = {3: (1, 1), 1: (0, 1), 2: (2, 1), 0: (2, 0), 4: (2, 2), 5: (0, 0), 6: (0, 2), 7: (1, 0), 8: (1, 2)}
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def put_dict2grid(dict, grid):
    for v in dict:
        s0, s1 = dict[v]
        grid[s0][s1] = v


put_dict2grid(dict, grid)
print(grid)
