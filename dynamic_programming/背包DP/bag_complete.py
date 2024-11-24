
# 内层循环中，从后往前遍历为01背包问题，从前往后遍历为完全背包问题
# 完全背包问题：
# 先遍历物品，再遍历背包容量，为组合数
# 先遍历背包容量，再遍历物品，为排列数

# 完全背包问题的状态转移方程：
# dp[i][j] = dp[i-1][j] + dp[i][j-w[i]]
# 其中，dp[i][j]表示前i件物品恰好装入一个容量为j的背包可以获得的最大价值
# dp[i-1][j]表示不选择第i件物品，前i-1件物品恰好装入一个容量为j的背包可以获得的最大价值
# dp[i][j-w[i]]表示选择第i件物品，前i件物品恰好装入一个容量为j-w[i]的背包可以获得的最大价值

# 01背包问题的状态转移方程：
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
# 其中，dp[i][j]表示前i件物品恰好装入一个容量为j的背包可以获得的最大价值
# dp[i-1][j]表示不选择第i件物品，前i-1件物品恰好装入一个容量为j的背包可以获得的最大价值
# dp[i-1][j-w[i]] + v[i]表示选择第i件物品，前i-1件物品恰好装入一个容量为j-w[i]的背包可以获得的最大价值，再加上第i件物品的价值v[i]


def bag_complete_recursive(n, w, v, capacity):
    pass


def bag_complete(n, w, v, capacity):
    dp = [[0] * (capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if w[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])
    return dp[n][capacity]


    


if __name__ == '__main__':
    n = 3
    w = [1, 2, 3]
    v = [1, 1, 1]
    capacity = 4
    print('bag_complete: ',bag_complete(n, w, v, capacity))