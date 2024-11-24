#
# * 159. 至多包含两个不同字符的最长子串
# 给你一个字符串 s ，请你找出 至多 包含 两个不同字符 的最长子串，并返回该子串的长度。

# 示例 1：
# 输入：s = "eceba"
# 输出：3
# 解释：满足题目要求的子串是 "ece" ，长度为 3 。
# 示例 2：
# 输入：s = "ccaabbb"
# 输出：5
# 解释：满足题目要求的子串是 "aabbb" ，长度为 5 。
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """滑动窗口"""
        n = len(s)
        cnt = defaultdict(int)  # 窗口内字符计数器
        collected = 0  # 窗口内收集到字符的种类数量
        ans, right = 0, -1

        for left, ch in enumerate(s):
            while right + 1 < n and collected <= 2:
                cnt[s[right + 1]] += 1
                if cnt[s[right + 1]] == 1:
                    collected += 1
                right += 1
                if collected <= 2:
                    ans = max(ans, right - left + 1)

            cnt[ch] -= 1
            if cnt[ch] == 0:
                collected -= 1
        return ans

    def lengthOfLongestSubstringTwoDistinct2(self, s: str) -> int:
        """另一种写法"""
        ans = 0
        cnt = defaultdict(int)  # 窗口内字符计数器
        collected = 0  # 窗口内收集到字符的种类数量
        left = 0

        for right, ch in enumerate(s):
            cnt[ch] += 1
            if cnt[ch] == 1:
                collected += 1
            while left <= right and collected > 2:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    collected -= 1
                left += 1
            # if collected <= 2:
            ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "eceba"
    print(sol.lengthOfLongestSubstringTwoDistinct(s))
    print(sol.lengthOfLongestSubstringTwoDistinct2(s))

    s = "ccaabbb"
    print(sol.lengthOfLongestSubstringTwoDistinct(s))
    print(sol.lengthOfLongestSubstringTwoDistinct2(s))
