# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 示例 1:
# 输入：prices = [3,3,5,0,0,3,1,4]
# 输出：6
# 解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

# 示例 2：
# 输入：prices = [1,2,3,4,5]
# 输出：4
# 解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

# 示例 3：
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
# 示例 4：
# 输入：prices = [1]
# 输出：0
from functools import cache


def maxProfit_two_times(prices: list[int]) -> int:

    # dp[i][0] 表示第 i 天第一次不持有股票的最大利润
    # dp[i][1] 表示第 i 天第一次持有股票的最大利润
    # dp[i][2] 表示第 i 天第二次不持有股票的最大利润
    # dp[i][3] 表示第 i 天第二次持有股票的最大利润
    dp = [[0, 0, 0, 0] for _ in range(len(prices))]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[0][2] = 0
    dp[0][3] = -prices[0]
    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], -prices[i])
        dp[i][2] = max(dp[i - 1][2], dp[i - 1][3] + prices[i])
        dp[i][3] = max(dp[i - 1][3], dp[i - 1][0] - prices[i])
    return dp[-1][2]


def maxProfit_k_times(prices: list[int], times: int) -> int:
    # dp[i][k] 表示第 i 天第k次不持有股票的最大利润
    # dp[i][k+1] 表示第 i 天第k次持有股票的最大利润
    dp = [[0] * (2 * times) for _ in range(len(prices))]
    for i in range(1, 2 * times, 2):
        dp[0][i] = -prices[0]
    for i in range(1, len(prices)):
        for k in range(0, 2 * times, 2):
            dp[i][k] = max(dp[i - 1][k], dp[i - 1][k + 1] + prices[i])
            if k - 2 < 0:
                dp[i][k + 1] = max(dp[i - 1][k + 1], -prices[i])
            else:
                dp[i][k + 1] = max(dp[i - 1][k + 1], dp[i - 1][k - 2] - prices[i])
    # print(dp)
    return dp[-1][times]


def maxProfit_k_times_re(prices: list[int], times: int) -> int:

    n = len(prices)

    @cache
    def dfs(i, k, hold):
        if k < 0:
            return float("-inf")
        if i < 0:
            return float("-inf") if hold else 0
        if hold:
            return max(dfs(i - 1, k, hold), dfs(i - 1, k, not hold) - prices[i])
        else:
            return max(dfs(i - 1, k, hold), dfs(i - 1, k - 1, not hold) + prices[i])

    return dfs(n - 1, times, False)


def maxProfit_k_times_dp(prices: list[int], times: int) -> int:

    n = len(prices)
    dp = [[[float("-inf")] * 2 for _ in range(times + 2)] for _ in range(n + 1)]
    for j in range(1, times + 2):
        dp[0][j][0] = 0
    for i, p in enumerate(prices):
        for j in range(1, times + 2):
            dp[i + 1][j][0] = max(dp[i][j][0], dp[i][j - 1][1] + p)
            dp[i + 1][j][1] = max(dp[i][j][1], dp[i][j][0] - p)

    return dp[n][times + 1][0]


def maxProfit_k_times_dp_improved(prices: list[int], times: int) -> int:

    # n = len(prices)
    dp = [[float("-inf")] * 2 for _ in range(times + 2)]
    for j in range(1, times + 2):
        dp[j][0] = 0
    for p in prices:
        for j in range(times + 1, 0 ,-1):
            dp[j][1] = max(dp[j][1], dp[j][0] - p)
            dp[j][0] = max(dp[j][0], dp[j - 1][1] + p)

    return dp[times + 1][0]


if __name__ == "__main__":
    # prices = [3, 3, 5, 0, 0, 3, 1, 4]
    # print(maxProfit_two_times(prices))  # 6

    # prices = [1, 2, 3, 4, 5]
    # print(maxProfit_two_times(prices))  # 4

    # prices = [7, 6, 4, 3, 1]
    # print(maxProfit_two_times(prices))  # 0

    # prices = [1]
    # print(maxProfit_two_times(prices))  # 0

    # print()

    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print(maxProfit_k_times(prices, 2))  # 6
    print(maxProfit_k_times_dp(prices, 2))
    print(maxProfit_k_times_dp_improved(prices, 2))
    print()

    prices = [1, 2, 3, 4, 5]
    print(maxProfit_k_times(prices, 2))  # 4
    print(maxProfit_k_times_dp(prices, 2))
    print(maxProfit_k_times_dp_improved(prices, 2))
    print()

    prices = [7, 6, 4, 3, 1]
    print(maxProfit_k_times(prices, 2))  # 0
    print(maxProfit_k_times_dp(prices, 2))
    print(maxProfit_k_times_dp_improved(prices, 2))
    print()

    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    print(maxProfit_k_times(prices, 4))  # 15
    print(maxProfit_k_times_dp(prices, 4))
    print(maxProfit_k_times_dp_improved(prices, 4))
    print()
