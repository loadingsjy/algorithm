# 639. 解码方法 II - H

# 一条包含字母 A-Z 的消息通过以下的方式进行了 编码 ：
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# 要 解码 一条已编码的消息，所有的数字都必须分组，然后按原来的编码方案反向映射回字母（可能存在多种方式）。例如，"11106" 可以映射为：
# "AAJF" 对应分组 (1 1 10 6)
# "KJF" 对应分组 (11 10 6)
# 注意，像 (1 11 06) 这样的分组是无效的，因为 "06" 不可以映射为 'F' ，因为 "6" 与 "06" 不同。
# 除了 上面描述的数字字母映射方案，编码消息中可能包含 '*' 字符，可以表示从 '1' 到 '9' 的任一数字（不包括 '0'）。例如，编码字符串 "1*" 可以表示 "11"、"12"、"13"、"14"、"15"、"16"、"17"、"18" 或 "19" 中的任意一条消息。对 "1*" 进行解码，相当于解码该字符串可以表示的任何编码消息。
# 给你一个字符串 s ，由数字和 '*' 字符组成，返回 解码 该字符串的方法 数目 。
# 由于答案数目可能非常大，返回 109 + 7 的 模 。

# 示例 1：
# 输入：s = "*"
# 输出：9
# 解释：这一条编码消息可以表示 "1"、"2"、"3"、"4"、"5"、"6"、"7"、"8" 或 "9" 中的任意一条。
# 可以分别解码成字符串 "A"、"B"、"C"、"D"、"E"、"F"、"G"、"H" 和 "I" 。
# 因此，"*" 总共有 9 种解码方法。
# 示例 2：
# 输入：s = "1*"
# 输出：18
# 解释：这一条编码消息可以表示 "11"、"12"、"13"、"14"、"15"、"16"、"17"、"18" 或 "19" 中的任意一条。
# 每种消息都可以由 2 种方法解码（例如，"11" 可以解码成 "AA" 或 "K"）。
# 因此，"1*" 共有 9 * 2 = 18 种解码方法。
# 示例 3：
# 输入：s = "2*"
# 输出：15
# 解释：这一条编码消息可以表示 "21"、"22"、"23"、"24"、"25"、"26"、"27"、"28" 或 "29" 中的任意一条。
# "21"、"22"、"23"、"24"、"25" 和 "26" 由 2 种解码方法，但 "27"、"28" 和 "29" 仅有 1 种解码方法。
# 因此，"2*" 共有 (6 * 2) + (3 * 1) = 12 + 3 = 15 种解码方法。

# 提示：
# 1 <= s.length <= 105
# s[i] 是 0 - 9 中的一位数字或字符 '*'

from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        """记忆化搜索"""
        n = len(s)
        mod = 10**9 + 7

        @cache
        def dfs(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0

            # 单独编码
            res = dfs(i + 1) * (9 if s[i] == "*" else 1)

            # 与后面那个字符一起编码
            if i + 1 < n:  #  i + 1 位置字符存在
                # 分类讨论
                if s[i] != "*" and s[i + 1] != "*":
                    if ((ord(s[i]) - ord("0")) * 10 + ord(s[i + 1]) - ord("0")) <= 26:
                        res += dfs(i + 2)
                elif s[i] != "*" and s[i + 1] == "*":
                    if s[i] == "1":
                        res += 9 * dfs(i + 2)
                    elif s[i] == "2":
                        res += 6 * dfs(i + 2)
                elif s[i] == "*" and s[i + 1] != "*":
                    if s[i + 1] <= "6":
                        res += 2 * dfs(i + 2)
                    else:
                        res += dfs(i + 2)
                elif s[i] == "*" and s[i + 1] == "*":
                    res += 15 * dfs(i + 2)
            return res % mod

        return dfs(0) % mod

    def numDecodings2(self, s: str) -> int:
        """动态规划"""
        if s[0] == "0":
            return 0
        mod = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1] * (9 if s[i - 1] == "*" else 1)
            if i > 1 and s[i - 2] != "0":
                # 分类讨论
                if s[i - 2] != "*" and s[i - 1] != "*":
                    if (
                        (ord(s[i - 2]) - ord("0")) * 10 + ord(s[i - 1]) - ord("0")
                    ) <= 26:
                        dp[i] += dp[i - 2]
                elif s[i - 2] != "*" and s[i - 1] == "*":
                    if s[i - 2] == "1":
                        dp[i] += 9 * dp[i - 2]
                    elif s[i - 2] == "2":
                        dp[i] += 6 * dp[i - 2]
                elif s[i - 2] == "*" and s[i - 1] != "*":
                    if s[i - 1] <= "6":
                        dp[i] += 2 * dp[i - 2]
                    else:
                        dp[i] += dp[i - 2]
                elif s[i - 2] == "*" and s[i - 1] == "*":
                    dp[i] += 15 * dp[i - 2]
            dp[i] %= mod
        return dp[n] % mod

    def numDecodings3(self, s: str) -> int:
        """动态规划 空间优化"""
        if s[0] == "0":
            return 0
        mod = 10**9 + 7
        n = len(s)
        # lastlast = f[i-2], last = f[i-1], cur = f[i]
        lastlast, last, cur = 0, 1, 0
        for i in range(1, n + 1):
            cur = 0
            if s[i - 1] != "0":
                cur += last * (9 if s[i - 1] == "*" else 1)
            if i > 1 and s[i - 2] != "0":
                # 分类讨论
                if s[i - 2] != "*" and s[i - 1] != "*":
                    if (
                        (ord(s[i - 2]) - ord("0")) * 10 + ord(s[i - 1]) - ord("0")
                    ) <= 26:
                        cur += lastlast
                elif s[i - 2] != "*" and s[i - 1] == "*":
                    if s[i - 2] == "1":
                        cur += 9 * lastlast
                    elif s[i - 2] == "2":
                        cur += 6 * lastlast
                elif s[i - 2] == "*" and s[i - 1] != "*":
                    if s[i - 1] <= "6":
                        cur += 2 * lastlast
                    else:
                        cur += lastlast
                elif s[i - 2] == "*" and s[i - 1] == "*":
                    cur += 15 * lastlast
            lastlast, last = last, cur % mod
        return cur % mod


if __name__ == "__main__":
    sol = Solution()
    s = "*10*1"
    print(sol.numDecodings(s))
    print(sol.numDecodings2(s))
    print(sol.numDecodings3(s))

    s = "904"
    print(sol.numDecodings(s))
    print(sol.numDecodings2(s))
    print(sol.numDecodings3(s))
