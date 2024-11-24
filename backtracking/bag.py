# 给定物品的重量和价值，背包的容量，求背包问题的最大价值。

# 动态规划法：
# 设dp[i][j]表示前i件物品恰好装入一个容量为j的背包可以获得的最大价值。
# 状态转移方程：
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i])
# 初始条件：dp[0][0] = 0
# 边界条件：dp[i][0] = 0
# 结果：dp[n][capacity]


# 递归法：
# 递归函数process_bag(weights, values, capacity,i,already_weight,already_value)
# 输入：weights, values, capacity,i,already_weight,already_value
# 输出：前i件物品恰好装入一个容量为capacity的背包可以获得的最大价值
# 递归终止条件：i == len(weights)
# 递归函数返回：already_value
# 递归函数返回：max(process_bag(weights, values, capacity,i+1,already_weight+weights[i],already_value+values[i]),
#                process_bag(weights, values, capacity,i+1,already_weight,already_value))


def process_bag(weights, values, capacity, i, already_weight, already_value):
    if already_weight > capacity:
        return 0
    if i == len(weights):
        return already_value

    return max(
        process_bag(
            weights,
            values,
            capacity,
            i + 1,
            already_weight + weights[i],
            already_value + values[i],
        ),
        process_bag(weights, values, capacity, i + 1, already_weight, already_value),
    )


def bag_problem(weights, values, capacity):
    return process_bag(weights, values, capacity, 0, 0, 0)


# Example usage:
if __name__ == "__main__":
    weights = [2, 3, 4, 5, 6]
    values = [1, 2, 3, 4, 5]
    capacity = 7
    print(bag_problem(weights, values, capacity))
