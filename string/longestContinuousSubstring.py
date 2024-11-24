#
# * 2414. 最长的字母序连续子字符串的长度 - M

# 字母序连续字符串 是由字母表中连续字母组成的字符串。换句话说，字符串 "abcdefghijklmnopqrstuvwxyz" 的任意子字符串都是 字母序连续字符串 。
# 例如，"abc" 是一个字母序连续字符串，而 "acb" 和 "za" 不是。
# 给你一个仅由小写英文字母组成的字符串 s ，返回其 最长 的 字母序连续子字符串 的长度。

# 示例 1：
# 输入：s = "abacaba"
# 输出：2
# 解释：共有 4 个不同的字母序连续子字符串 "a"、"b"、"c" 和 "ab" 。
# "ab" 是最长的字母序连续子字符串。
# 示例 2：
# 输入：s = "abcde"
# 输出：5
# 解释："abcde" 是最长的字母序连续子字符串。

# 提示：
# 1 <= s.length <= 10^5
# s 由小写英文字母组成

from itertools import pairwise


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        length = 1
        ans = 0
        for i in range(1, n):
            if ord(s[i]) == ord(s[i - 1]) + 1:
                length += 1
            else:
                ans = max(ans, length)
                length = 1
        ans = max(ans, length)
        return ans

    def longestContinuousSubstring2(self, s: str) -> int:
        """灵神写法"""
        ans = cnt = 1
        for x, y in pairwise(map(ord, s)):
            cnt = cnt + 1 if x + 1 == y else 1
            ans = max(ans, cnt)
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "abacaba"
    print(sol.longestContinuousSubstring(s))
    print(sol.longestContinuousSubstring2(s))

    s = "abcde"
    print(sol.longestContinuousSubstring(s))
    print(sol.longestContinuousSubstring2(s))
