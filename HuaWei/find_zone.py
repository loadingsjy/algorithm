def is_board(m, n, coordinate):
    x = coordinate[0]
    y = coordinate[1]
    return x == 0 or x == m - 1 or y == 0 or y == n - 1


def find_board_neighbors(m, n, x, y):
    neighbors = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
    res = []
    for ne in neighbors:
        if is_board(m, n, ne):
            res.append(m, n, ne)
    return res


# x, y 为当前坐标(x和y必有一个是0或x==n-1或y==m-1)，coordinate为结果
def find_zone(m, n, mat, x, y, coordinate):
    # 判断是否为单入口
    
    for ne in find_board_neighbors(m, n, x, y):
        if mat[ne[0]][ne[1]] == 'O':
            return 
