# 给你一个字符串 s，找到 s 中回文子串的个数。
# 回文子串是指从左往右读和从右往左读都是一样的字符串。
# 示例 1：
# 输入：s = "abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
# 示例 2：
# 输入：s = "aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

from functools import cache


@cache
def isPalindrome(i: int, j: int) -> int:
    if i >= j:
        return 1
    return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1


def Palindrome(s: str) -> bool:

    count = 0
    n = len(s)
    # dp[i][j] 表示 s[i:j+1] 是否为回文串，保证j>=i
    dp = [[False] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):  # 注意这里的 j 要从 i 开始
            if s[i] == s[j]:
                if j - i <= 1:  # 就一个字符，即dp的对角线设置为True
                    dp[i][j] = True
                    count += 1
                elif dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                    count += 1
    return count


if __name__ == "__main__":
    s = "aaa"
    print(Palindrome(s))
    s = "ababc"
    print(Palindrome(s))
