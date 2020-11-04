def connect_vertices_in_line(vertices):
    return [(vertices[i], vertices[i + 1]) for i in range(len(vertices) - 1)]


vertices = (0, 1, 2, 3, 4, 5, 6, 7, 8)
width = 3
height = 3
# vertices = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
# width = 4
# height = 4
edges = connect_vertices_in_line(vertices)
print(edges)
horizontal_lines = [vertices[i * width: (i + 1) * width] for i in range(height)]
print(horizontal_lines)  # [(0, 1, 2), (3, 4, 5), (6, 7, 8)]

# line1 = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
# line2 = [(3, 4, 5), (6, 7, 8)]
for line1, line2 in zip(horizontal_lines, horizontal_lines[1:]):
    # line1[:-1] 取line1的索引0~倒数第二索引位
    # line2[1:0] 取line2的索引1~最后一位
    new_edges = [(v1, v2) for v1, v2 in zip(line1[:-1], reversed(line2[1:]))]  # 第一次 line1[:-1]=[0, 1], reversed(line2[1:] = [5, 4]
    edges.extend(new_edges) # 第一次 new_edges = [(0, 5), (1, 4)]
print(edges)
