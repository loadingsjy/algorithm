#
# * 688. 骑士在棋盘上的概率 - M

# 在一个 n x n 的国际象棋棋盘上，一个骑士从单元格 (row, column) 开始，并尝试进行 k 次移动。行和列是 从 0 开始 的，所以左上单元格是 (0,0) ，右下单元格是 (n - 1, n - 1) 。
# 象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。
# 每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。
# 骑士继续移动，直到它走了 k 步或离开了棋盘。
# 返回 骑士在棋盘停止移动后仍留在棋盘上的概率 。

# 示例 1：
# 输入: n = 3, k = 2, row = 0, column = 0
# 输出: 0.0625
# 解释: 有两步(到(1,2)，(2,1))可以让骑士留在棋盘上。
# 在每一个位置上，也有两种移动可以让骑士留在棋盘上。
# 骑士留在棋盘上的总概率是0.0625。
# 示例 2：
# 输入: n = 1, k = 0, row = 0, column = 0
# 输出: 1.00000
# 提示:
# 1 <= n <= 25
# 0 <= k <= 100
# 0 <= row, column <= n - 1

from functools import cache


class Solution:

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        @cache
        def dfs(i, j, steps):
            if i < 0 or j < 0 or i >= n or j >= n:
                return 0.0
            if steps == 0:
                return 1.0

            ans = 0.0
            ans += dfs(i + 2, j + 1, steps - 1) / 8.0
            ans += dfs(i + 2, j - 1, steps - 1) / 8.0
            ans += dfs(i - 2, j + 1, steps - 1) / 8.0
            ans += dfs(i - 2, j - 1, steps - 1) / 8.0
            ans += dfs(i + 1, j + 2, steps - 1) / 8.0
            ans += dfs(i + 1, j - 2, steps - 1) / 8.0
            ans += dfs(i - 1, j + 2, steps - 1) / 8.0
            ans += dfs(i - 1, j - 2, steps - 1) / 8.0

            return ans

        return dfs(row, column, k)

    def knightProbability2(self, n: int, k: int, row: int, column: int) -> float:
        """DP + 空间压缩"""
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1

        directions = [
            (1, 2),
            (1, -2),
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (-1, 2),
            (-1, -2),
        ]

        for _ in range(k):
            new_dp = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if dp[i][j] != 0:
                        for d in directions:
                            x, y = i + d[0], j + d[1]
                            if 0 <= x < n and 0 <= y < n:
                                new_dp[x][y] += dp[i][j]

            dp = new_dp

        return sum(map(sum, dp)) / float(8**k)


if __name__ == "__main__":
    sol = Solution()
    n = 3
    k = 2
    row = 0
    column = 0
    print(sol.knightProbability(n, k, row, column))
    print(sol.knightProbability2(n, k, row, column))
