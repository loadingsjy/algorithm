# 给定一个字符串 s，请将 s 分割成一些子串，使每个子串都是回文串。
# 返回符合要求的 最少分割次数 。

# 示例 1：
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
# 示例 2：
# 输入：s = "a"
# 输出：0
# 示例 3：
# 输入：s = "ab"
# 输出：1

import random


class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0
        return self.cut(s, 0)

    def is_palindrome(self, s):
        return s == s[::-1]

    def is_palindrome_dp(self, s):
        n = len(s)
        record = [[False] * n for _ in range(n)]
        for i in range(n - 1):
            record[i][i] = True
            if s[i] == s[i + 1]:
                record[i][i + 1] = True
        for row in range(n - 3, -1, -1):
            for col in range(row + 2, n):
                if s[row] == s[col] and record[row + 1][col - 1]:
                    record[row][col] = True
        return record

    def cut(self, s, i):
        """暴力递归 str[...i]最少能分割成多少回文的部分 时间复杂度O(N**3)"""
        if i == len(s):
            return 0

        # 尝试每一个end，如果str[i..end]这个部分是回文，就去尝试这个部分是作为回文的第一块
        ans = float("inf")
        for end in range(i, len(s)):
            if self.is_palindrome(s[i : end + 1]):
                # str[i...]被拆分成：str[i...end] 和 str[end+1...]两部分 怎么拆最省
                ans = min(ans, self.cut(s, end + 1) + 1)
        return ans

    def minCut_dp(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[n - 1] = 1
        record = self.is_palindrome_dp(s)
        for i in range(n - 2, -1, -1):
            dp[i] = n - i  # 每个字符当做一个回文串，最大分割
            for j in range(i, n):
                if record[i][j]:
                    dp[i] = min(dp[i], dp[j + 1] + 1)
        return dp[0]


if __name__ == "__main__":
    s = Solution()
    string = "sadaasadfd"
    # 分割部分 = 分割次数 + 1
    print(s.minCut(string) - 1, s.minCut_dp(string) - 1)

    # 对数器
    count = 100
    for j in range(count):
        length = random.randint(1, 1000) % 100
        string = "".join([chr(ord("a") + random.randint(0, 25)) for i in range(length)])
        if s.minCut(string) != s.minCut_dp(string):
            print("error!")
            print("string: ", string)
            print(s.minCut(string), s.minCut_dp(string))
            print()
            break

    if j >= count - 1:
        print("success!")
