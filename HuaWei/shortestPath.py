# 小王是一名基站维护工程师，负责某区域的基站维护。某地方有n个基站(1<n<10)，已知各基站之间的距离s(0<s<500)并且基站到
# 基站y的距离，与基站y到基站的距离并不一定会相同。小王从基站1出发，途经每个基站1次，然后返回基站1,需要请你为他选择一条距离最短的路。
# 输入描述
# 站点数n和各站点之间的距离(均为整数)。
# 如:
# 3站点数
# 0 2 1 站点1到各站点的路程]
# 1 0 2 站点2到各站点的路程]
# 2 1 0 (站点3到各站点的路程
# 输出描述
# 最短路Q程的数值
# 示例1:
# 输入:
# 3
# 0 2 1
# 1 0 2
# 2 1 0
# 输出:
# 3


def shortestPath(n, matrix):
    MAX = 1 << n  # 状态压缩
    # dp[i][j]表示从i出发经过的基站的集合为j所用的最短距离
    dp = [[float("inf")] * MAX for _ in range(n)]
    for i in range(n):
        dp[i][1 << i] = matrix[0][i]

    for j in range(MAX):  # 遍历状态
        for i in range(n):  # 遍历基站
            if (j & (1 << i)) == 0:  # i这个基站不在j状态中，也就是对当前状态i不可达
                continue

            for k in range(n):  # 从k出发经过j中所有基站除了i的最短距离+k到i的距离
                dp[i][j] = min(dp[i][j], dp[k][j ^ (1 << i)] + matrix[k][i])
    print(dp)
    return dp[0][MAX - 1]


if __name__ == "__main__":
    n = 3
    mat = [[0, 2, 1], [1, 0, 2], [2, 1, 0]]
    print(shortestPath(n, mat))
