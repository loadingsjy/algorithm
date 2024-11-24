# 机器人走格子问题
# 题目描述：
# N长度的数组(起始位置的索引是1，1~n)，每个位置表示一个格子，机器人从一个start格子开始，走到end位置的格子，必须走K步，每步只能向左或向右走一步
# 问从起始格子到达终止格子，有多少种走路的方法数？


# 暴力递归
# 时间复杂度：O(2^k)
# 空间复杂度：O(1)
def walk_ways_recursive(n, end, rest, cur):
    """
    # N：一共是1~n的n个格子，固定参数
    # end：终止位置，固定参数
    # rest：还剩rest步要走，可变参数
    # cur：当前位置，从1到N，可变参数
    # 返回值：方法数
    """
    if rest == 0:
        return 1 if cur == end else 0
    if cur == 1:
        return walk_ways_recursive(n, end, rest - 1, 2)
    if cur == n:
        return walk_ways_recursive(n, end, rest - 1, n - 1)

    return walk_ways_recursive(n, end, rest - 1, cur - 1) + walk_ways_recursive(
        n, end, rest - 1, cur + 1
    )


# 优化：带缓存的暴力递归
# 时间复杂度：O(k*n)
# 空间复杂度：O(k*n)
def walk_ways_recursive_cache(n, end, rest, cur, dp):
    if dp[rest][cur] != -1:
        return dp[rest][cur]

    if rest == 0:
        dp[rest][cur] = 1 if cur == end else 0
        return dp[rest][cur]

    if cur == 1:
        dp[rest][cur] = walk_ways_recursive_cache(n, end, rest - 1, 2, dp)
    elif cur == n:
        dp[rest][cur] = walk_ways_recursive_cache(n, end, rest - 1, n - 1, dp)
    else:
        dp[rest][cur] = walk_ways_recursive_cache(
            n, end, rest - 1, cur - 1, dp
        ) + walk_ways_recursive_cache(n, end, rest - 1, cur + 1, dp)
    return dp[rest][cur]


# 动态规划
# 时间复杂度：O(k*n)
# 空间复杂度：O(k*n)
def walk_ways_dp(n, start, end, k):
    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
    dp[0][start] = 1
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if j == 1:
                dp[i][j] = dp[i - 1][2]
            elif j == n:
                dp[i][j] = dp[i - 1][n - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
    return dp[k][end]


if __name__ == "__main__":
    n = 5
    start = 2
    end = 4
    k = 4
    dp = [[-1 for _ in range(n + 1)] for _ in range(k + 1)]
    print(walk_ways_recursive(n, end, k, start))
    print(walk_ways_recursive_cache(n, end, k, start, dp))
    print(walk_ways_dp(n, start, end, k))

    n = 10
    start = 3
    end = 7
    k = 8
    dp = [[-1 for _ in range(n + 1)] for _ in range(k + 1)]
    print(walk_ways_recursive(n, end, k, start))
    print(walk_ways_recursive_cache(n, end, k, start, dp))
    print(walk_ways_dp(n, start, end, k))
