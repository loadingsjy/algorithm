#
# * 115. 不同的子序列 - H
# 给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数，结果需要对 109 + 7 取模。

# 示例 1：
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# rabbbit
# rabbbit
# rabbbit
# 示例 2：
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下所示, 有 5 种可以从 s 中得到 "bag" 的方案。
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag

# 提示：
# 1 <= s.length, t.length <= 1000
# s 和 t 由英文字母组成


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """动态规划：
        dp[i][j] 代表 T前i个字符串可以由S前j个字符串组成最多个数
        所以动态方程:
        当 S[j] == T[i] , dp[i][j] = dp[i-1][j-1] + dp[i][j-1];
        当 S[j] != T[i] , dp[i][j] = dp[i][j-1]
        """
        n1 = len(s)
        n2 = len(t)
        # dp[i][j] 代表 T前i个字符串可以由S前j个字符串组成最多个数
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        for j in range(n1 + 1):
            dp[0][j] = 1
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                dp[i][j] = dp[i][j - 1]
                if t[i - 1] == s[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        # print(dp)
        return dp[-1][-1]

    def numDistinct2(self, s: str, t: str) -> int:
        """空间压缩"""
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [1] + [0] * n
        for c in s:
            for j in range(n, 0, -1):
                if c == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]
