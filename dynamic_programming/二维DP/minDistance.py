#
# * 72. 编辑距离  - M
# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符

# 示例 1：
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2：
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')

# 提示：
# 0 <= word1.length, word2.length <= 500
# word1 和 word2 由小写英文字母组成


from functools import cache


class Solution:

    def minDistance1(self, s: str, t: str) -> int:
        """记忆化搜索"""
        n, m = len(s), len(t)

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if s[i] == t[j]:
                return dfs(i - 1, j - 1)
            return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1

        return dfs(n - 1, m - 1)

    def minDistance2(self, word1: str, word2: str) -> int:
        """动态规划"""
        m, n = len(word1), len(word2)
        # dp[i][j] 表示 A 的前 i 个字母和 B 的前 j 个字母之间的编辑距离
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[m][n]

    def minDistance3(self, word1: str, word2: str) -> int:
        """空间压缩"""
        m, n = len(word1), len(word2)
        # dp[i][j] 表示 A 的前 i 个字母和 B 的前 j 个字母之间的编辑距离
        dp = list(range(n + 1))
        for i in range(1, m + 1):
            leftUp = dp[0]
            dp[0] += 1
            for j in range(1, n + 1):
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = leftUp
                else:
                    dp[j] = 1 + min(dp[j], dp[j - 1], leftUp)
                leftUp = temp

        return dp[-1]

    def minDistance(self, s: str, t: str) -> int:
        """灵神写法"""
        f = list(range(len(t) + 1))
        for x in s:
            pre = f[0]
            f[0] += 1
            for j, y in enumerate(t):
                tmp = f[j + 1]
                f[j + 1] = pre if x == y else min(f[j + 1], f[j], pre) + 1
                pre = tmp
        return f[-1]
