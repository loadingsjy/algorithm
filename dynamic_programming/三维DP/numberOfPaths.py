#
# * 2435. 矩阵中和能被 K 整除的路径 - H
# 给你一个下标从 0 开始的 m x n 整数矩阵 grid 和一个整数 k 。你从起点 (0, 0) 出发，每一步只能往 下 或者往 右 ，你想要到达终点 (m - 1, n - 1) 。
# 请你返回路径和能被 k 整除的路径数目，由于答案可能很大，返回答案对 109 + 7 取余 的结果。
# 提示：

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 5 * 104
# 1 <= m * n <= 5 * 104
# 0 <= grid[i][j] <= 100
# 1 <= k <= 50

from functools import cache


class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        """记忆化搜索 有BUG"""
        MOD = 10**9 + 7
        n, m = len(grid), len(grid[0])

        @cache
        def dfs(i, j, r):
            if i == n - 1 and j == m - 1:
                return int((grid[i][j] + r) % k == 0)
            need = (r - grid[i][j] % k + k) % k
            ans = 0
            if i + 1 < n:
                ans += dfs(i + 1, j, need)
            if j + 1 < m:
                ans = (ans + dfs(i, j + 1, need)) % MOD
            return ans

        ans = dfs(0, 0, 0)
        dfs.cache_clear()
        return ans

    def numberOfPaths2(self, grid: list[list[int]], k: int) -> int:
        """记忆化搜索 灵神版本"""
        MOD = 10**9 + 7
        n, m = len(grid), len(grid[0])

        @cache
        def dfs(i, j, v):
            """从(i,j)出发，当前路径和模k的结果为v时符合题目要求的路径个数"""
            if i < 0 or j < 0:
                return 0
            v = (v + grid[i][j]) % k
            if i == j == 0:
                return int(v == 0)
            return (dfs(i - 1, j, v) + dfs(i, j - 1, v)) % MOD

        ans = dfs(n - 1, m - 1, 0)
        dfs.cache_clear()
        return ans

    def numberOfPaths3(self, grid: list[list[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        f = [[[0] * k for _ in range(n + 1)] for _ in range(m + 1)]
        f[0][1][0] = 1
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                for v in range(k):
                    f[i + 1][j + 1][(v + x) % k] = (
                        f[i + 1][j][v] + f[i][j + 1][v]
                    ) % MOD
        return f[m][n][0]
