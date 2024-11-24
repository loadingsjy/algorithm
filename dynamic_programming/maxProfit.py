# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 示例 1:
# 输入: prices = [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
# 示例 2:
# 输入: prices = [1]
# 输出: 0

from math import inf
from functools import cache


# 可以买卖多次（无限次）。
def maxProfit_re_cache(prices: list[int]) -> int:
    """递归搜索 + 保存计算结果 = 记忆化搜索"""
    n = len(prices)

    @cache  # 缓存装饰器，避免重复计算 dfs 的结果
    def dfs(i: int, hold: bool) -> int:
        if i < 0:
            return -inf if hold else 0
        if hold:
            return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
        return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])

    return dfs(n - 1, False)


def maxProfit_dp(prices: list[int]) -> int:
    """1:1 翻译成递推"""
    n = len(prices)
    # dp[i][0] 表示第 i 天不持有股票的最大利润(两种情况：之前也不持有，之前持有)
    # dp[i][1] 表示第 i 天持有股票的最大利润（两种情况：之前也持有，之前不持有）
    f = [[0] * 2 for _ in range(n + 1)]
    f[0][1] = -inf
    for i, p in enumerate(prices):
        f[i + 1][0] = max(f[i][0], f[i][1] + p)
        f[i + 1][1] = max(f[i][1], f[i][0] - p)
    return f[n][0]


def maxProfit_dp_improved(prices) -> int:
    """空间优化"""
    dp = [0, 0]
    dp[1] = -prices[0]
    for p in prices:
        dp[0] = max(dp[0], dp[1] + p)
        dp[1] = max(dp[1], dp[0] - p)
    return dp[0]


def maxProfit_dp_improved2(prices) -> int:
    """空间优化2"""
    dp0 = 0
    dp1 = -prices[0]
    for p in prices:
        new_dp0 = max(dp0, dp1 + p)
        dp1 = max(dp1, dp0 - p)
        dp0 = new_dp0
    return dp0


def maxProfit_greedy(prices):
    """贪心的角度考虑我们每次选择贡献大于 0 的区间即能使得答案最大化，因此最后答案为ans= i=1∑n−1 max{0,a[i]−a[i−1]}其中 n 为数组的长度。
    需要说明的是，贪心算法只能用于计算最大利润，计算的过程并不是实际的交易过程。"""
    ans = 0
    n = len(prices)
    for i in range(1, n):
        ans += max(0, prices[i] - prices[i - 1])
    return ans


# 可以买卖多次（无限次），空窗期为 freeze 天, free为手续费(买入股票时扣除)。
def maxProfit_f(prices, freeze=0, free=0) -> int:
    # dp[i][0] 表示第 i 天不持有股票的最大利润(两种情况：之前也不持有，之前持有)
    # dp[i][1] 表示第 i 天持有股票的最大利润（两种情况：之前也持有，之前不持有）
    dp = [[0, 0] for _ in range(len(prices))]
    dp[0][0] = 0
    dp[0][1] = -prices[0] - free
    for i in range(1, len(prices)):
        # 第 i 天不持有股票的最大利润 = max(第 i-1 天不持有股票的最大利润，第 i-1 天持有股票的最大利润 + 第 i 天的价格)
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        # 第 i 天持有股票的最大利润 = max(第 i-1 天持有股票的最大利润，第 i-1-freeze 天不持有股票的最大利润 - 第 i 天的价格) 冷冻期为 freeze 天
        dp[i][1] = max(dp[i - 1][1], dp[i - 1 - freeze][0] - prices[i] - free)
    # 最后一天不持有股票的最大利润一定比最后一天持有股票的最大利润大，所以返回最后一天不持有股票的最大利润
    return dp[-1][0]


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4, 6, 3, 4]

    print(maxProfit_re_cache(prices))
    print(maxProfit_dp(prices))
    print(maxProfit_dp_improved(prices))
    print(maxProfit_dp_improved2(prices))
    print(maxProfit_greedy(prices))
    print()

    print("手续费为 0：, 冷冻期为 0 天：")
    print(maxProfit_f(prices, freeze=0, free=0))

    print("手续费为 1：, 冷冻期为 0 天：")
    print(maxProfit_f(prices, freeze=0, free=1))

    print("手续费为 0：, 冷冻期为 3 天：")
    print(maxProfit_f(prices, freeze=3, free=0))
