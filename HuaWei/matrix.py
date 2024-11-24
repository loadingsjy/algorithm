# 给定一块n*m的地块，相当于n*m的二维数组，每个元素的值表示这个小地块的发电量，求在这块地上建立正方形的边长为c的发电站，发电站满足目标电量的地块数量。


def construct_presuffix(mat):
    """构建前缀和矩阵"""
    row_n = len(mat)
    col_n = len(mat[0])

    presuffix = [[0] * col_n for _ in range(row_n)]

    presuffix[0][0] = mat[0][0]

    for i in range(1, row_n):
        presuffix[i][0] = mat[i][0] + presuffix[i - 1][0]
    for j in range(1, col_n):
        presuffix[0][j] = mat[0][j] + presuffix[0][j - 1]

    for i in range(1, row_n):
        for j in range(1, col_n):
            presuffix[i][j] = (
                presuffix[i - 1][j]
                + presuffix[i][j - 1]
                - presuffix[i - 1][j - 1]
                + mat[i][j]
            )
    return presuffix


def numOfSquare(mat, c, k):
    ans = 0
    presuffix = construct_presuffix(mat)
    # assert n == len(mat) and m == len(mat[0])
    # 遍历所有可能边长为c的正方形，(i,j)为正方形右下角的坐标
    for i in range(c - 1, n):
        for j in range(c - 1, m):
            ld = presuffix[i - c][j] if i - c >= 0 else 0
            ru = presuffix[i][j - c] if j - c >= 0 else 0
            lu = presuffix[i - c][j - c] if i - c >= 0 and j - c >= 0 else 0
            s = presuffix[i][j] - ld - ru + lu
            if s >= k:
                ans += 1
    return ans


if __name__ == "__main__":
    n, m, c, k = 3, 5, 2, 12
    mat = [[1, 3, 4, 5, 8], [2, 3, 6, 7, 1], [4, 1, 5, 1, 2]]
    print(numOfSquare(mat, c, k))
