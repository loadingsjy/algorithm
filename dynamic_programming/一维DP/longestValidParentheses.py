#
# * 32. 最长有效括号 - H
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

# 示例 1：
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
# 示例 2：
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"

# 提示：
# 0 <= s.length <= 3 * 104
# s[i] 为 '(' 或 ')'


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        # dp[i] = 子串 必须以s[i]为结尾的 最长有效括号子串的长度
        dp = [0] * n
        for i, cur in enumerate(s):
            if cur == ")":
                pre = i - dp[i - 1] - 1
                if pre >= 0 and s[pre] == "(":
                    dp[i] = dp[i - 1] + 2 + (dp[pre - 1] if pre - 1 >= 0 else 0)
        return max(dp)
