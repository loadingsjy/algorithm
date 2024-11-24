# 给定一个n*n的矩阵Matrix，其中只有0和1两种值，返回边框全是1的最大正方形的边长长度。

# 暴力枚举，先穷举所有所有的正方形矩阵，然后验证边界上的值是否都是1，如果是，则计算周长，取最大值。时间复杂度O(n^4)
# 得到所有可能正方形矩阵时间复杂度O(n^3),验证边界上的值时间复杂度O(n),总复杂度O(n^4)
def maxbRroadSize(grid):
    n = len(grid)
    m = len(grid[0])    # 矩阵的边长
    max_size = 0
    max_square = None
    for i in range(n-1):
        for j in range(m-1):
            # 遍历所有可能的正方形矩阵
            for k in range(i, n):
                for l in range(j, m):
                    # 验证边界上的值是否都是1
                    if all(grid[x][y] == 1 for x in range(i, k+1) for y in range(j, l+1)):
                        # 计算周长
                        size = (k-i+1) * (l-j+1)
                        if size > max_size:
                            max_size = size
                            max_square = (i, j)
    return max_size, max_square

# 优化，构建后缀连续1的数量矩阵和下缀连续1的数量矩阵，验证边界上的值是否都是1的时间复杂度降低到O(1)，
# 只须验证后缀矩阵和下缀矩三个顶点的值是否大于等于边长即可，总复杂度O(n^3)
def maxbRroadSize(grid):
    n = len(grid)
    m = len(grid[0])    # 矩阵的边长
    max_size = 0
    max_square = None
    # 构建后缀连续1的数量矩阵
    suffix_count = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m-1, -1, -1):
            if grid[i][j] == 1:
                suffix_count[i][j] = 1 + suffix_count[i][j+1] if j+1 < m else 1
    # 构建下缀连续1的数量矩阵
    prefix_count = [[0] * m for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(m):
            if grid[i][j] == 1:
                prefix_count[i][j] = 1 + prefix_count[i+1][j] if i+1 < n else 1
    # 验证边界上的值是否都是1
    for i in range(n-1):
        for j in range(m-1):
            if suffix_count[i][j+1] >= n-i-1 and prefix_count[i+1][j] >= m-j-1:
                # 计算周长
                size = (n-i-1) * (m-j-1)
                if size > max_size:
                    max_size = size
                    max_square = (i, j)
    return max_size, max_square


if __name__ == '__main__':
    # 测试
    grid = [
        [0, 1, 1, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    print(maxbRroadSize(grid))  # (9, (1, 1))
    print(maxbRroadSize(grid))  # (9, (0, 0))