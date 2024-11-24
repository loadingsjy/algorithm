# 给定物品的重量和价值，背包的容量，求背包问题的最大价值。

# 动态规划法：
# 设dp[i][j]表示前i件物品恰好装入一个容量为j的背包可以获得的最大价值。
# 状态转移方程：
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i])
# 初始条件：dp[0][0] = 0
# 边界条件：dp[i][0] = 0
# 结果：dp[n][capacity]

# 时间复杂度：O(n*capacity)
# 空间复杂度：O(n*capacity)

def bag_problem(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            dp[i][j] = dp[i-1][j]                                           # 不装入第i件物品
            if j >= weights[i-1]:                                          # 装入第i件物品
                dp[i][j] = max(dp[i][j], dp[i-1][j-weights[i-1]] + values[i-1])         # 选择装入第i件物品或不装入

    return dp[n][capacity]


# 优化空间复杂度,只使用一维数组，空间复杂度为O(capacity)
def bag_problem_improved(weights, values, capacity):
    n = len(weights)
    # dp[i]背包容量为i时，可以获得最大价值
    dp = [0] * (capacity+1)    # 优化空间复杂度
    for i in range(1, n+1):
        for j in range(capacity, weights[i-1]-1, -1):       # 逆序遍历，避免重复计算
            dp[j] = max(dp[j], dp[j-weights[i-1]] + values[i-1])
    return dp[capacity]



# Example usage:
if __name__ == '__main__':
    weights = [2, 3, 4, 5, 6]
    values = [1, 2, 3, 4, 5]
    capacity = 7
    print(bag_problem(weights, values, capacity))
    print(bag_problem_improved(weights, values, capacity))
