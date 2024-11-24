#
# * 64. 最小路径和 - M

# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。
# 示例 1：
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
# 示例 2：
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12

# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200

from math import inf
from itertools import accumulate


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """动态规划"""
        n, m = len(grid), len(grid[0])
        # dp[i][j] =  从(0,0)点到达(i, j)点的 最小路径和
        dp = [[inf] * m for _ in range(n)]

        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        # print(dp)

        return dp[n - 1][m - 1]

    def minPathSum2(self, grid: list[list[int]]) -> int:
        """动态规划，空间压缩  每行dp[i-1]自我更新成dp[i]"""
        n, m = len(grid), len(grid[0])
        dp = list(accumulate(grid[0]))
        for i in range(1, n):
            dp[0] += grid[i][0]
            for j in range(1, m):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(sol.minPathSum(grid))
    print(sol.minPathSum2(grid))
