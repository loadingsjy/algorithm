#
# * 329. 矩阵中的最长递增路径 - H
# 给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。
# 示例 2：
# 输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
# 输出：4
# 解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
# 示例 3：
# 输入：matrix = [[1]]
# 输出：1

# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 2^31 - 1
from functools import cache, lru_cache
from math import inf


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        @cache
        def dfs(i, j):
            length = 1
            if i > 0 and matrix[i - 1][j] > matrix[i][j]:
                length = max(length, dfs(i - 1, j) + 1)

            if i < n - 1 and matrix[i + 1][j] > matrix[i][j]:
                length = max(length, dfs(i + 1, j) + 1)

            if j > 0 and matrix[i][j - 1] > matrix[i][j]:
                length = max(length, dfs(i, j - 1) + 1)

            if j < m - 1 and matrix[i][j + 1] > matrix[i][j]:
                length = max(length, dfs(i, j + 1) + 1)

            return length

        ans = -inf
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))
        return ans

    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath2(self, matrix: list[list[int]]) -> int:
        if not matrix:
            return 0

        @lru_cache(None)
        def dfs(row: int, column: int) -> int:
            best = 1
            for dx, dy in Solution.DIRS:
                newRow, newColumn = row + dx, column + dy
                if (
                    0 <= newRow < rows
                    and 0 <= newColumn < columns
                    and matrix[newRow][newColumn] > matrix[row][column]
                ):
                    best = max(best, dfs(newRow, newColumn) + 1)
            return best

        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans


if __name__ == "__main__":
    sol = Solution()
    matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    print(sol.longestIncreasingPath(matrix))
    print(sol.longestIncreasingPath2(matrix))
