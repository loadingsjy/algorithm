
# 最后一块石头的重量
# 题目描述：有一堆石头，每块石头的重量都是正整数。
# 每次将两个石头一起粉碎，重量较轻的一块石头就被完全粉碎。
# 最后剩下的石头，我们称之为最后一块石头。
# 问最后一块石头的重量。


# 动态规划解法：
# 将石头看成重量和价值相等、背包容量为(sum//2)的01背包问题，得到的最大价值将石头分成两部分，将两部分相减，得到最后一块石头的重量。
def lastStoneWeight(stones):
    target = sum(stones)//2
    n = len(stones)
    dp = [0] * (target+1)
    for i in range(1, n+1):
        for j in range(target, stones[i-1]-1, -1):
            dp[j] = max(dp[j], dp[j-stones[i-1]]+stones[i-1])
    
    return sum(stones) - 2* dp[target]



if __name__ == '__main__':
    # 输入：stones = [2,7,4,1,8,1]
    # 输出：1
    # 解释：
    # 先将 7 和 8 粉碎，得到 1，再将 2 和 4 粉碎，得到 1，再将 1 和 1 粉碎，得到 0，最后剩下 1 块石头。
    stones = [2, 7, 4, 1, 8, 1]
    print(lastStoneWeight(stones))  # 1