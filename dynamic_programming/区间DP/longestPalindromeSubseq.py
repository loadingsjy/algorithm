#
# * 516. 最长回文子序列 - M
# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

# 示例 1：
# 输入：s = "bbbab"
# 输出：4
# 解释：一个可能的最长回文子序列为 "bbbb" 。
# 示例 2：
# 输入：s = "cbbd"
# 输出：2
# 解释：一个可能的最长回文子序列为 "bb" 。

# 提示：
# 1 <= s.length <= 1000
# s 仅由小写英文字母组成

# * 也可以将问题转化为s和逆序串s'的最长公共子序列的长度

from functools import cache


def longestPalindromeSubseq1(s: str) -> int:
    """记忆化搜索"""

    @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
    def dfs(i: int, j: int) -> int:
        if i > j:
            return 0  # 空串
        if i == j:
            return 1  # 只有一个字母
        if s[i] == s[j]:
            return dfs(i + 1, j - 1) + 2  # 都选
        return max(dfs(i + 1, j), dfs(i, j - 1))  # 枚举哪个不选

    return dfs(0, len(s) - 1)


def longestPalindromeSubseq2(s: str) -> str:
    n = len(s)
    # dp[i][j] 表示 s[i...j] 中最长回文子串的长度
    dp = [[0] * n for _ in range(n)]

    # 以自己为中心的回文子串长度为 1
    for i in range(n):
        dp[i][i] = 1

    # 从左下角开始计算
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


def longestPalindromeSubseq3(s: str) -> str:
    """动态规划：空间优化 自我更新成 i-1 行的数据"""
    n = len(s)
    dp = [1] * n

    # 从左下角开始计算
    for i in range(n - 1, -1, -1):
        leftDown = 0
        for j in range(i + 1, n):
            temp = dp[j]
            if s[i] == s[j]:
                dp[j] = leftDown + 2
            else:
                dp[j] = max(dp[j], dp[j - 1])
            leftDown = temp

    return dp[-1]


if __name__ == "__main__":
    s = "babad"
    print(longestPalindromeSubseq1(s))
    print(longestPalindromeSubseq2(s))
    print(longestPalindromeSubseq3(s))

    s = "cbbdca"
    print(longestPalindromeSubseq1(s))
    print(longestPalindromeSubseq2(s))
    print(longestPalindromeSubseq3(s))

    s = "abc"
    print(longestPalindromeSubseq1(s))
    print(longestPalindromeSubseq2(s))
    print(longestPalindromeSubseq3(s))
