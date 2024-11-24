# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
# 你可以认为每种硬币的数量是无限的。
from math import inf
from functools import cache


class Solution:

    def coinChange_minCoinsNumber_cache(self, coins: list[int], amount: int) -> int:
        """递归搜索 + 保存计算结果 = 记忆化搜索"""

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, c: int) -> int:
            if i < 0:
                return 0 if c == 0 else inf
            if c < coins[i]:
                return dfs(i - 1, c)

            return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)

        ans = dfs(len(coins) - 1, amount)
        return ans if ans < inf else -1

    def coinChange_dp(self, coins: list[int], amount: int) -> int:
        """1:1 翻译成递推"""
        n = len(coins)
        f = [[inf] * (amount + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i, x in enumerate(coins):
            for c in range(amount + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = min(f[i][c], f[i + 1][c - x] + 1)
        ans = f[n][amount]
        return ans if ans < inf else -1

    def coinChange_dp_improved(self, coins: list[int], amount: int) -> int:
        """空间优化：两个数组（滚动数组）"""
        n = len(coins)
        f = [[inf] * (amount + 1) for _ in range(2)]
        f[0][0] = 0
        for i, x in enumerate(coins):
            for c in range(amount + 1):
                if c < x:
                    f[(i + 1) % 2][c] = f[i % 2][c]
                else:
                    f[(i + 1) % 2][c] = min(f[i % 2][c], f[(i + 1) % 2][c - x] + 1)
        ans = f[n % 2][amount]
        return ans if ans < inf else -1

    def coinChange_minCoinsNumber_(self, coins, amount):
        """空间优化：一个数组"""
        # dp[i] 表示凑够 i 金额所需的最少硬币个数
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1

    def coin_change_greedy(self, coins: list[int], amt: int) -> int:
        """零钱兑换：贪心，不一定是最优解"""
        # 假设 coins 列表有序
        i = len(coins) - 1
        count = 0
        # 循环进行贪心选择，直到无剩余金额
        while amt > 0:
            # 找到小于且最接近剩余金额的硬币
            while i > 0 and coins[i] > amt:
                i -= 1
            # 选择 coins[i]
            amt -= coins[i]
            count += 1
        # 若未找到可行方案，则返回 -1
        return count if amt == 0 else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    s = Solution()
    print(s.coinChange_minCoinsNumber(coins, amount))  # Output: 3
    # print(s.coin_change_greedy(coins, amount))

    print(s.coinChange_ways_recursive(coins, amount))
    print(s.coinChange_ways_dp(coins, amount))
    print(s.coinChange_ways_dp_improved(coins, amount))

    print(s.change(coins, amount))
