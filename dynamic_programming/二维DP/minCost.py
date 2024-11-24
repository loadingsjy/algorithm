#
# * 256. 粉刷房子 - M
# 假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
# 当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的正整数矩阵 costs 来表示的。
# 例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，以此类推。
# 请计算出粉刷完所有房子最少的花费成本。

# 示例 1：
# 输入: costs = [[17,2,17],[16,16,5],[14,3,19]]
# 输出: 10
# 解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。
#      最少花费: 2 + 5 + 3 = 10。
# 示例 2：
# 输入: costs = [[7,6,2]]
# 输出: 2

# 提示:
# costs.length == n
# costs[i].length == 3
# 1 <= n <= 100
# 1 <= costs[i][j] <= 20

import copy
from math import inf


class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        """动态规划"""
        # dp[i][j] 代表 粉刷0....i房子 且 第i个房子粉刷color[j] 的最小花费
        n, m = len(costs), len(costs[0])
        dp = [[0] * m for _ in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            for j in range(m):
                dp[i][j] = (
                    min([dp[i - 1][k] if k != j else inf for k in range(m)])
                    + costs[i][j]
                )
        return min(dp[-1])

    def minCost(self, costs: list[list[int]]) -> int:
        """动态规划 空间压缩"""
        n, m = len(costs), len(costs[0])
        prev = costs[0]
        for i in range(1, n):
            cur = [0] * m
            for j in range(m):
                cur[j] = (
                    min([prev[k] if k != j else inf for k in range(m)]) + costs[i][j]
                )
            prev = cur
        return min(prev)

    def minCost(self, costs: list[list[int]]) -> int:
        """动态规划 空间压缩 简洁版"""
        n = len(costs)
        dp = [0, 0, 0]
        for i in range(n):
            a, b, c = dp
            dp[0] = min(b, c) + costs[i][0]
            dp[1] = min(a, c) + costs[i][1]
            dp[2] = min(a, b) + costs[i][2]

        return min(dp)
