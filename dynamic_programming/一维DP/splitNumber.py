import random
# 将数字n分裂成和为n的序列，序列以递增排序，求n所有可能的分裂数

def spiltNumber_re(num):
    if num < 1:
        return 0
    return process(1, num)


# pre:上一次裂开的值
# rest:当前剩余的值需要去裂开，要求裂开出来的第一部分，不要比pre小
# 返回裂开的方法数
def process(pre, rest):
    if rest == 0:
        return 1
    if pre > rest:
        return 0

    ways = 0
    for i in range(pre, rest + 1):
        ways += process(i, rest - i)

    return ways


def spiltNumber_dp(n):
    if n < 1:
        return 0
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = 1
    for pre in range(n, 0, -1):
        for rest in range(pre, n + 1):
            for i in range(pre, rest + 1):
                dp[pre][rest] += dp[i][rest - i]
    return dp[1][n]


def spiltNumber_dp_improved(n):
    if n < 1:
        return 0
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = 1
        
    for i in range(1, n + 1):
        dp[i][i] = 1
    
    for pre in range(n - 1, 0, -1):
        for rest in range(pre + 1, n + 1):
            # 斜率优化
            dp[pre][rest] = dp[pre + 1][rest] + dp[pre][rest - pre]
    
    return dp[1][n]


if __name__ == "__main__":
    num = 10
    print(spiltNumber_re(num), spiltNumber_dp(num), spiltNumber_dp_improved(num))

    # 对数器
    # count = 10
    # for j in range(count):
    #     num = random.randint(1, 1000) % 100
    #     p1 = spiltNumber_re(num)
    #     p2 = spiltNumber_dp(num)
    #     p3 = spiltNumber_dp_improved(num)
    #     if p1 != p2 or p2 != p3:
    #         print("error!")
    #         print("number : ", num)
    #         print(spiltNumber_re(num), spiltNumber_dp(num), spiltNumber_dp_improved(num))
    #         print()

    # if j >= count - 1:
    #     print("success!")
