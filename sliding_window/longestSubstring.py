#
# * 395. 至少有 K 个重复字符的最长子串
# 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
# 如果不存在这样的子字符串，则返回 0。

# 示例 1：
# 输入：s = "aaabb", k = 3
# 输出：3
# 解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
# 示例 2：
# 输入：s = "ababbc", k = 2
# 输出：5
# 解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

# 提示：
# 1 <= s.length <= 104
# s 仅由小写英文字母组成
# 1 <= k <= 105
import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """先确定了种类数量才能用滑动窗口，保证窗口滑动的单调性"""
        # kinds = len(set(list(s)))
        n = len(s)
        ans = 0
        for require in range(1, 27):
            cnts = collections.defaultdict(int)
            left = 0
            collect, staisfy = 0, 0
            # collect: 窗口中一共收集到的种类数
            # satisfy: 窗口中达标（次数>=k）的种类数
            for right in range(n):
                cnts[s[right]] += 1
                if cnts[s[right]] == 1:
                    collect += 1
                if cnts[s[right]] == k:
                    staisfy += 1

                # 种类超了，left位置的字符需要去掉
                while collect > require:
                    if cnts[s[left]] == 1:
                        collect -= 1
                    if cnts[s[left]] == k:
                        staisfy -= 1
                    cnts[s[left]] -= 1
                    left += 1

                if staisfy == require:
                    ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "aaabb"
    k = 3
    print(sol.longestSubstring(s, k))

    s = "ababbc"
    k = 2
    print(sol.longestSubstring(s, k))
