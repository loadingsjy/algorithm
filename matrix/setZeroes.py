# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。


def setZeroes(self, matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # 思路：
    # 1. 遍历矩阵，将所有值为 0 的行和列的索引记录下来。
    # 2. 遍历矩阵，将所有值为 0 的行的元素设为 0，将所有值为 0 的列的元素设为 0。

    row_len = len(matrix)
    col_len = len(matrix[0])
    row_zero = set()
    col_zero = set()
    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == 0:
                row_zero.add(i)
                col_zero.add(j)

    for i in range(row_len):
        for j in range(col_len):
            if i in row_zero or j in col_zero:
                matrix[i][j] = 0


def setZeroes2(self, matrix: list[list[int]]) -> None:
    """思路和算法:
    我们可以用矩阵的第一行和第一列代替方法一中的两个标记数组，以达到 O(1) 的额外空间。
    但这样会导致原数组的第一行和第一列被修改，无法记录它们是否原本包含 0。
    因此我们需要额外使用两个标记变量分别记录第一行和第一列是否原本包含 0。

    在实际代码中，我们首先预处理出两个标记变量，接着使用其他行与列去处理第一行与第一列，
    然后反过来使用第一行与第一列去更新其他行与列，最后使用两个标记变量更新第一行与第一列即可。"""
    m, n = len(matrix), len(matrix[0])
    flag_col0 = any(matrix[i][0] == 0 for i in range(m))
    flag_row0 = any(matrix[0][j] == 0 for j in range(n))

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if flag_col0:
        for i in range(m):
            matrix[i][0] = 0

    if flag_row0:
        for j in range(n):
            matrix[0][j] = 0
