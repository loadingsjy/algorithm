# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
# "1" -> 'A'
# "2" -> 'B'
# ...
# "25" -> 'Y'
# "26" -> 'Z'
# 然而，在 解码 已编码的消息时，你意识到有许多不同的方式来解码，因为有些编码被包含在其它编码当中（"2" 和 "5" 与 "25"）。
# 例如，"11106" 可以映射为：
# "AAJF" ，将消息分组为 (1, 1, 10, 6)
# "KJF" ，将消息分组为 (11, 10, 6)
# 消息不能分组为  (1, 11, 06) ，因为 "06" 不是一个合法编码（只有 "6" 是合法的）。
# 注意，可能存在无法解码的字符串。
# 给你一个只含数字的 非空 字符串 s ，请计算并返回解码方法的总数 。如果没有合法的方式解码整个字符串，返回 0。
# 题目数据保证答案肯定是一个 32 位 的整数。

# 示例 1：
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2：
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 示例 3：
# 输入：s = "06"
# 输出：0
# 解释："06" 无法映射到 "F" ，因为存在前导零（"6" 和 "06" 并不等价）。
from functools import cache


def numDecodings_recursive(s: str) -> int:
    @cache
    def dfs(i):
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0

        # 单独编码
        res = dfs(i + 1)
        # 与后面那个字符一起编码
        if i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6")):
            res += dfs(i + 2)

        return res

    return dfs(0)


def numDecodings(s: str) -> int:
    n = len(s)
    # 字符串 s 的前 i 个字符 s[0..i-1] 的解码方法数
    f = [1] + [0] * n
    for i in range(1, n + 1):
        if s[i - 1] != "0":
            f[i] += f[i - 1]
        if i > 1 and s[i - 2] != "0" and int(s[i - 2 : i]) <= 26:
            f[i] += f[i - 2]
    return f[n]


def numDecodings2(s: str) -> int:
    n = len(s)
    s = " " + s
    # 字符串 s 的前 i 个字符 s[0..i] 的解码方法数
    f = [0] * (n + 1)
    f[0] = 1  # 空字符串有一种解码方式
    for i in range(1, n + 1):
        a = ord(s[i]) - ord("0")
        b = (ord(s[i - 1]) - ord("0")) * 10 + a
        if 1 <= a <= 9:
            f[i] = f[i - 1]
        if i - 2 >= 0 and 10 <= b <= 26:
            f[i] += f[i - 2]
    return f[n]


def numDecodings3(s: str) -> int:
    """空间优化 ： 注意到在状态转移方程中，fi的值仅与 fi−1和 fi−2有关，因此我们可以使用三个变量进行状态转移，省去数组的空间。"""
    n = len(s)
    # lastlast = f[i-2], last = f[i-1], cur = f[i]
    lastlast, last, cur = 0, 1, 0
    for i in range(1, n + 1):
        cur = 0
        if s[i - 1] != "0":
            cur += last
        if i > 1 and s[i - 2] != "0" and int(s[i - 2 : i]) <= 26:
            cur += lastlast
        lastlast, last = last, cur
    return cur


if __name__ == "__main__":
    s = "1232671"
    print(numDecodings_recursive(s))
    print(numDecodings(s))
    print(numDecodings2(s))
    print(numDecodings3(s))
    print()

    s = "2261231"
    print(numDecodings_recursive(s))
    print(numDecodings(s))
    print(numDecodings2(s))
    print(numDecodings3(s))
    print()

    s = "10234"
    print(numDecodings_recursive(s))
    print(numDecodings(s))
    print(numDecodings2(s))
    print(numDecodings3(s))
