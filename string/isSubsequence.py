#
# *392. 判断子序列

# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
# 进阶：
# 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
# 致谢：
# 特别感谢 @pbrother 添加此问题并且创建所有测试用例。

# 示例 1：
# 输入：s = "abc", t = "ahbgdc"
# 输出：true
# 示例 2：
# 输入：s = "axc", t = "ahbgdc"
# 输出：false


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """双指针法"""
        n = len(s)
        m = len(t)
        i, j = 0, 0
        while i < n and j < m:
            if s[i] != t[j]:
                j += 1
            else:
                i += 1
                j += 1
        return i == n

    def isSubsequence2(self, s: str, t: str) -> bool:
        """动态规划预处理
        该解法中对 t 的处理与 s 无关，且预处理完成后，可以利用预处理数组的信息，线性地算出任意一个字符串 s 是否为 t 的子串。
        这样我们就可以解决「后续挑战」啦。"""
        n, m = len(s), len(t)
        # dp[i][j] 表示字符串 t 中从位置 i 开始往后字符 j 第一次出现的位置
        dp = [[0] * 26 for _ in range(m)]
        dp.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                dp[i][j] = i if ord(t[i]) == j + ord("a") else dp[i + 1][j]

        add = 0
        for i in range(n):
            if dp[add][ord(s[i]) - ord("a")] == m:
                return False
            add = dp[add][ord(s[i]) - ord("a")] + 1

        return True

    def isSubsequence3(self, s, t):
        """队列的思想。ptr模拟s字符串的队头，每当有一个匹配的字符出队一次，最终队列为空则s字符串能匹配t字符串。时间复杂度N空间复杂度1"""
        ptr = 0  # 模拟队头指针
        n, m = len(s), len(t)
        if n == 0:
            return True
        for i in range(m):
            if t[i] == s[ptr]:
                ptr += 1
            if ptr == n:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    t = "ahbgdc"
    print(sol.isSubsequence(s, t))
    print(sol.isSubsequence2(s, t))
    print(sol.isSubsequence3(s, t))
