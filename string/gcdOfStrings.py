#
# * 1071. 字符串的最大公因子 - E
# 对于字符串 s 和 t，只有在 s = t + t + t + ... + t + t（t 自身连接 1 次或多次）时，我们才认定 “t 能除尽 s”。
# 给定两个字符串 str1 和 str2 。返回 最长字符串 x，要求满足 x 能除尽 str1 且 x 能除尽 str2 。

# 示例 1：
# 输入：str1 = "ABCABC", str2 = "ABC"
# 输出："ABC"
# 示例 2：
# 输入：str1 = "ABABAB", str2 = "ABAB"
# 输出："AB"
# 示例 3：
# 输入：str1 = "LEET", str2 = "CODE"
# 输出：""

# 提示：
# 1 <= str1.length, str2.length <= 1000
# str1 和 str2 由大写英文字母组成

import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """先求出最长公共前缀，判断这个前缀是否为公因子"""

        def check(s, p):
            """返回 p字符串是否是s的 重复子串"""
            if len(s) % len(p):
                return False
            return s == p * (len(s) // len(p))

        if str1 == str2:
            return str1

        n, m = len(str1), len(str2)
        i = 0
        prefix = ""
        while i < n and i < m:
            if str1[i] == str2[i]:
                prefix += str1[i]
            else:
                break
            i += 1

        while prefix:
            if check(str1, prefix) and check(str2, prefix):
                return prefix
            else:
                prefix = prefix[:-1]
        return ""

    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        """如果存在一个符合要求的字符串 X，那么也一定存在一个符合要求的字符串 X'，它的长度为 str1 和 str2 长度的最大公约数。"""

        candidate_len = math.gcd(len(str1), len(str2))
        candidate = str1[:candidate_len]
        if (
            candidate * (len(str1) // candidate_len) == str1
            and candidate * (len(str2) // candidate_len) == str2
        ):
            return candidate
        return ""

    def gcdOfStrings3(self, str1: str, str2: str) -> str:
        """str1 和 str2 拼接后等于 str2和 str1 拼接起来的字符串（注意拼接顺序不同）<===> 一定存在符合题目条件的字符串 X。(充分必要条件)"""
        candidate_len = math.gcd(len(str1), len(str2))
        candidate = str1[:candidate_len]
        if str1 + str2 == str2 + str1:
            return candidate
        return ""


if __name__ == "__main__":
    sol = Solution()
    str1 = "ABCABC"
    str2 = "ABC"
    print(sol.gcdOfStrings(str1, str2))
    print(sol.gcdOfStrings2(str1, str2))
    print(sol.gcdOfStrings3(str1, str2))
