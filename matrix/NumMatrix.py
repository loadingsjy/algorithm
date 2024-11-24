#
# * 二维区域和检索-矩阵不可变

# 给定一个二维矩阵 matrix，以下类型的多个请求：

# 计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。
# 实现 NumMatrix 类：

# NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
# int sumRegion(int row1, int col1, int row2, int col2) 返回 左上角 (row1, col1) 、右下角 (row2, col2) 所描述的子矩阵的元素 总和 。


class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.pre_sum = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                self.pre_sum[i + 1][j + 1] = (
                    self.pre_sum[i][j + 1]
                    + self.pre_sum[i + 1][j]
                    - self.pre_sum[i][j]
                    + matrix[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.pre_sum[row2 + 1][col2 + 1]
            - self.pre_sum[row1][col2 + 1]
            - self.pre_sum[row2 + 1][col1]
            + self.pre_sum[row1][col1]
        )


if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]

    m = NumMatrix(matrix)
    print(m.sumRegion(2, 1, 4, 3))
    print(m.sumRegion(1, 1, 2, 2))
    print(m.sumRegion(1, 2, 2, 4))
