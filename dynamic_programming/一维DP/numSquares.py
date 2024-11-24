# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。


class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] 表示凑够 i 数所需的最少完全平方数的个数
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        # for i in range(1, n+1):
        #     dp[i] = float('inf')
        #     for j in range(1, int(i**0.5)+1):
        #         dp[i] = min(dp[i], dp[i-j*j]+1)
        i = 1
        while i * i <= n:
            for j in range(i * i, n + 1):
                dp[j] = min(dp[j], dp[j - i * i] + 1)
            i += 1
        return dp[n]


# 时间复杂度：O(n^1.5)
# 空间复杂度：O(n)

# 思路：
# 动态规划法，用 dp[i] 表示和为 i 的完全平方数的最少数量。
# 状态转移方程：dp[i] = min(dp[i], dp[i-j*j]+1)，其中 1 ≤ j ≤ i/2。
# 解释：如果 i 可以表示为 j^2 + k^2，其中 j 和 k 都是整数，那么 dp[i] = dp[i-j^2-k^2] + 1。
# 因为 j^2 + k^2 也是完全平方数，所以 dp[i-j^2-k^2] 也是一个完全平方数，且 dp[i-j^2-k^2] 已经计算过，所以可以直接用 dp[i-j^2-k^2] 加 1。
# 时间复杂度：O(n^1.5)
# 空间复杂度：O(n)

if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(12))  # 3
    print(s.numSquares(13))  # 2
    print(s.numSquares(14))  # 3
    print(s.numSquares(15))  # 4
    print(s.numSquares(16))  # 1
    print(s.numSquares(17))  # 2
