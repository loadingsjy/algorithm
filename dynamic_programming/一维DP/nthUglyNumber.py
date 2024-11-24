#
# * 264. 丑数 II - M

# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
# 丑数 就是质因子只包含 2、3 和 5 的正整数。

# 示例 1：
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
# 示例 2：
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。

# 提示：
# 1 <= n <= 1690


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * (n + 1)
        i2, i3, i5 = 1, 1, 1  # 当前*2、*3、*5的丑数在第几个丑数上
        for i in range(2, n + 1):
            a, b, c = dp[i2] * 2, dp[i3] * 3, dp[i5] * 5
            dp[i] = min(a, b, c)
            if dp[i] == a:
                i2 += 1
            if dp[i] == b:
                i3 += 1
            if dp[i] == c:
                i5 += 1
        return dp[n]
