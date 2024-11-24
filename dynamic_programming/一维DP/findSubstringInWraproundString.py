#
# * 467. 环绕字符串中唯一的子字符串 - M
# 定义字符串 base 为一个 "abcdefghijklmnopqrstuvwxyz" 无限环绕的字符串，所以 base 看起来是这样的：
# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
# 给你一个字符串 s ，请你统计并返回 s 中有多少 不同非空子串 也在 base 中出现。

# 示例 1：
# 输入：s = "a"
# 输出：1
# 解释：字符串 s 的子字符串 "a" 在 base 中出现。
# 示例 2：
# 输入：s = "cac"
# 输出：2
# 解释：字符串 s 有两个子字符串 ("a", "c") 在 base 中出现。
# 示例 3：
# 输入：s = "zab"
# 输出：6
# 解释：字符串 s 有六个子字符串 ("z", "a", "b", "za", "ab", and "zab") 在 base 中出现。

# 提示：
# 1 <= s.length <= 105
# s 由小写英文字母组成
from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        n = len(s)
        s = [ord(ch) - ord("a") for ch in s]
        # dp[i] = 必须以s[i]为结尾的 在base串中也出现的子串的最长长度
        dp = [1] * n
        for i in range(1, n):
            if s[i] == (s[i - 1] + 1) % 26:
                dp[i] = dp[i - 1] + 1

        # 去重： 只算每种字符的最大符合条件的长度
        ans = [0] * 26
        for i, idx in enumerate(s):
            ans[idx] = max(ans[idx], dp[i])
        return sum(ans)

    def findSubstringInWraproundString2(self, s: str) -> int:
        n = len(s)
        # s = [ord(ch) - ord("a") for ch in s]
        length = 1
        ans = [0] * 26
        ans[ord(s[0]) - ord("a")] = 1
        for i in range(1, n):
            idx = ord(s[i]) - ord("a")
            if (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
                length += 1
            else:
                length = 1
            ans[idx] = max(ans[idx], length)

        return sum(ans)

    def findSubstringInWraproundString3(self, p: str) -> int:
        """官方题解"""
        dp = defaultdict(int)
        k = 0
        for i, ch in enumerate(p):
            if i > 0 and (ord(ch) - ord(p[i - 1])) % 26 == 1:  # 字符之差为 1 或 -25
                k += 1
            else:
                k = 1
            dp[ch] = max(dp[ch], k)
        return sum(dp.values())


if __name__ == "__main__":
    sol = Solution()
    s = "zab"
    print(sol.findSubstringInWraproundString(s))
    print(sol.findSubstringInWraproundString2(s))
    print(sol.findSubstringInWraproundString3(s))
