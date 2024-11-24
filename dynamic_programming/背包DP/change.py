# 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
# 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
# 假设每一种面额的硬币有无限个。


class Solution:

    def coinChange_ways_re(self, coins, amount):
        # * 递归版本
        return self.dfs(coins, 0, amount)

    def dfs(self, coins, index, amount):
        if index == len(coins):
            return 1 if amount == 0 else 0
        ways = 0
        for i in range(amount // coins[index] + 1):  # i代表硬币个数
            ways += self.dfs(coins, index + 1, amount - i * coins[index])
        return ways

    def coinChange_ways_dp(self, coins, amount):
        """动态规划版本"""
        if not coins:
            return 0
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[n][0] = 1
        for row in range(n - 1, -1, -1):
            for col in range(0, amount + 1):
                ways = 0
                for i in range(col // coins[row] + 1):
                    ways += dp[row + 1][col - i * coins[row]]
                dp[row][col] = ways
        return dp[0][amount]

    def coinChange_ways_dp_improved(self, coins, amount):
        """动态规划斜率优化版本"""
        if not coins:
            return 0
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[n][0] = 1
        for row in range(n - 1, -1, -1):
            for col in range(0, amount + 1):
                dp[row][col] = dp[row + 1][col]
                if col - coins[row] >= 0:
                    dp[row][col] += dp[row][col - coins[row]]
        return dp[0][amount]

    def change(self, amount: int, coins: list[int]) -> int:
        # * 官方答案
        # 装满容量为j的背包，有dp[j]种方法
        dp = [0] * (amount + 1)
        dp[0] = 1
        # for coin in coins:
        #     for i in range(coin, amount + 1):
        #         dp[i] += dp[i - coin]

        # 内层循环中，从后往前遍历为01背包问题，从前往后遍历为完全背包问题
        # 完全背包问题：
        # 先遍历物品，再遍历背包容量，为组合数
        # 先遍历背包容量，再遍历物品，为排列数

        for i in range(1, len(coins) + 1):
            for j in range(coins[i - 1], amount + 1):
                dp[j] += dp[j - coins[i - 1]]

        return dp[amount]


if __name__ == "__main__":
    s = Solution()
    amount = 5
    coins = [1, 2, 5]
    print(s.coinChange_ways_re(coins, amount))
    print(s.coinChange_ways_dp(coins, amount))
    print(s.coinChange_ways_dp_improved(coins, amount))
    print(s.change(amount, coins))  # Output: 4
