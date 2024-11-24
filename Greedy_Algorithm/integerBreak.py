#
# * 343. 整数拆分 - M
# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
# 返回 你可以获得的最大乘积 。

# 示例 1:
# 输入: n = 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
# 示例 2:
# 输入: n = 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
# 提示: 2 <= n <= 58

import math


class Solution:
    def integerBreak(self, n: int) -> int:
        """数学思路： 假设一个数的其中一个最优因子为f>=4；则f可以拆解为2和f-2，则2*（f-2）=2f-4>=f;
        所以在寻求最大乘积时4不可以作为最优因子；所以当一个数大于4时他的最优因子可以包含1，2，3，但是一般3要多点，所以三尽可能的多；
        但是1一般是无效的只会出现2和3；

        即将数字 n 尽可能以因子 3 等分时，乘积最大。
        https://leetcode.cn/problems/integer-break/solutions/29098/343-zheng-shu-chai-fen-tan-xin-by-jyd/
        拆分规则：
        1.最优： 3 。把数字 n 可能拆为多个因子 3 ，余数可能为 0,1,2 三种情况。
        2.次优： 2 。若余数为 2 ；则保留，不再拆为 1+1 。
        3.最差： 1 。若余数为 1 ；则应把一份 3+1 替换为 2+2，因为 2×2 > 3×1。
        算法流程：
        1)当 n≤3 时，按照规则应不拆分，但由于题目要求必须拆分，因此必须拆出一个因子 1 ，即返回 n−1 。
        2)当 n>3 时，求 n 除以 3 的 整数部分 a 和 余数部分 b （即 n=3a+b ），并分为以下三种情况：
            1.当 b=0 时，直接返回 3^a；
            2.当 b=1 时，要将一个 1+3 转换为 2+2，因此返回 3^(a−1)×4；
            3.当 b=2 时，返回 3^a×2。
        """

        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)

    def integerBreak2(self, n: int) -> int:
        if n <= 3:
            return n - 1
        dp = [0] * 58
        dp[2] = 1
        dp[3] = 2
        dp[4] = 4
        dp[5] = 6
        dp[6] = 9
        for i in range(7, n + 1):
            dp[i] = max(3 * dp[i - 3], 2 * dp[i - 2])
        return dp[n]

    def integerBreak_dp(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]

    def integerBreak_dp_improved(self, n: int) -> int:
        if n <= 3:
            return n - 1

        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = max(2 * (i - 2), 2 * dp[i - 2], 3 * (i - 3), 3 * dp[i - 3])

        return dp[n]
