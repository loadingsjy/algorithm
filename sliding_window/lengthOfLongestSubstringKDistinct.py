#
# * 340. 至多包含 K 个不同字符的最长子串 - M
# 给你一个字符串 s 和一个整数 k ，请你找出 至多 包含 k 个 不同 字符的最长子串，并返回该子串的长度。

# 示例 1：
# 输入：s = "eceba", k = 2
# 输出：3
# 解释：满足题目要求的子串是 "ece" ，长度为 3 。
# 示例 2：
# 输入：s = "aa", k = 1
# 输出：2
# 解释：满足题目要求的子串是 "aa" ，长度为 2 。

# 提示：
# 1 <= s.length <= 5 * 104
# 0 <= k <= 50
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # n = len(s)
        # cnt = defaultdict(int)
        # collected = 0
        # ans = 0
        # right = -1
        # for left, ch in enumerate(s):
        #     while right + 1 < n and collected <= k:
        #         cnt[s[right + 1]] += 1
        #         if cnt[s[right + 1]] == 1:
        #             collected += 1
        #         right += 1
        #         if collected <= k:
        #             ans = max(ans, right - left + 1)
        #     cnt[ch] -= 1
        #     if cnt[ch] == 0:
        #         collected -= 1
        # return ans

        cnt = defaultdict(int)
        left, ans, collected = 0, 0, 0
        for right, ch in enumerate(s):
            cnt[ch] += 1
            if cnt[ch] == 1:
                collected += 1
            while left <= right and collected > k:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    collected -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "eceba"
    k = 2
    print(sol.lengthOfLongestSubstringKDistinct(s, k))
