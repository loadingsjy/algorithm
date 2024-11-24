#
# * 879. 盈利计划 - H
# 集团里有 n 名员工，他们可以完成各种各样的工作创造利润。
# 第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。
# 工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。
# 有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。

# 示例 1：
# 输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
# 输出：2
# 解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
# 总的来说，有两种计划。
# 示例 2：
# 输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
# 输出：7
# 解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
# 有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。

# 提示：
# 1 <= n <= 100
# 0 <= minProfit <= 100
# 1 <= group.length <= 100
# 1 <= group[i] <= 100
# profit.length == group.length
# 0 <= profit[i] <= 100

from functools import cache


MOD = 10**9 + 7


class Solution:

    def profitableSchemes(self, n, minProfit, group: list[int], profit: list[int]):
        """记忆化搜索"""

        # n = len(group)  # n 参数里用过了，会有bug
        @cache
        def dfs(i, p, staff):
            if i == len(group):  # 没有工作可选了
                return 1 if p == 0 else 0
            if staff <= 0:  # 没有员工了
                return 1 if p == 0 else 0
            # 不做当前工作
            res = dfs(i + 1, p, staff)
            # 要做当前工作
            if staff >= group[i]:
                res += dfs(i + 1, max(0, p - profit[i]), staff - group[i])
            return res % MOD

        return dfs(0, minProfit, n) % MOD

    def profitableSchemes2(self, n, minProfit, group: list[int], profit: list[int]):
        """动态规划"""
        m = len(group)  # n 参数里用过了
        dp = [[[0] * (n + 1) for _ in range(minProfit + 1)] for _ in range(m + 1)]

        for i in range(n + 1):
            dp[0][0][i] = 1

        for i in range(1, m + 1):
            for j in range(minProfit + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if k >= group[i - 1]:
                        dp[i][j][k] = (
                            dp[i][j][k]
                            + dp[i - 1][max(0, j - profit[i - 1])][k - group[i - 1]]
                        ) % MOD
        return dp[-1][-1][-1] % MOD

    def profitableSchemes3(self, n, minProfit, group: list[int], profit: list[int]):
        """空间压缩：两个二维平面滚动更新"""
        m = len(group)  # n 参数里用过了
        dp = [[[0] * (n + 1) for _ in range(minProfit + 1)] for _ in range(2)]

        for i in range(n + 1):
            dp[0][0][i] = 1

        for i in range(1, m + 1):
            for j in range(minProfit + 1):
                for k in range(n + 1):
                    dp[i % 2][j][k] = dp[(i - 1) % 2][j][k]
                    if k >= group[i - 1]:
                        dp[i % 2][j][k] += dp[(i - 1) % 2][max(0, j - profit[i - 1])][
                            k - group[i - 1]
                        ]
                    dp[i % 2][j][k] %= MOD
        return dp[m % 2][-1][-1] % MOD

    def profitableSchemes4(self, n, minProfit, group: list[int], profit: list[int]):
        """空间压缩：一维平面自我更新"""
        m = len(group)  # n 参数里用过了
        dp = [[0] * (n + 1) for _ in range(minProfit + 1)]

        for i in range(n + 1):
            dp[0][i] = 1

        for i in range(1, m + 1):
            for j in range(minProfit, -1, -1):
                for k in range(n, group[i - 1] - 1, -1):
                    dp[j][k] += dp[max(0, j - profit[i - 1])][k - group[i - 1]]
                    dp[j][k] %= MOD
        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    n = 10
    minProfit = 5
    group = [2, 3, 5]
    profit = [6, 7, 8]
    print(sol.profitableSchemes(n, minProfit, group, profit))
    print(sol.profitableSchemes2(n, minProfit, group, profit))
    print(sol.profitableSchemes3(n, minProfit, group, profit))
    print(sol.profitableSchemes4(n, minProfit, group, profit))
