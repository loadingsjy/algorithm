#
# * 424. 替换后的最长重复字符 - M
# 给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。
# 在执行上述操作后，返回 包含相同字母的最长子字符串的长度。

# 示例 1：
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个'A'替换为两个'B',反之亦然。
# 示例 2：
# 输入：s = "AABABBA", k = 1
# 输出：4
# 解释：
# 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。
# 可能存在其他的方法来得到同样的结果。

# 提示：
# 1 <= s.length <= 105
# s 仅由大写英文字母组成
# 0 <= k <= s.length

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """右边界先移动找到一个满足题意的可以替换 k 个字符以后，所有字符都变成一样的当前看来最长的子串，直到右边界纳入一个字符以后，不能满足的时候停下；
        然后考虑左边界向右移动，左边界只须要向右移动一格以后，右边界就又可以开始向右移动了，继续尝试找到更长的目标子串；
        替换后的最长重复子串就产生在右边界、左边界交替向右移动的过程中。"""

        """maxCount是当前及过去滑动窗口维护过的最大字符数，所以maxcount+k 是出现过的最大重复字符串数；
        当right- left ！= maxcount+k时，右移是没有意义的，所以左移，然后继续向右探索，
        窗口大小始终维持最大重复字符串数 因为比这小的也是没有意义的，所以42-43行可以删掉"""
        ans = 0
        cnts = defaultdict(int)  # 窗口内字符计数
        most_count = 0  # 窗口内数量最多的某个字符的数量
        left = 0
        for right, ch in enumerate(s):
            cnts[ch] += 1
            if cnts[ch] > most_count:
                most_count = cnts[ch]

            while left <= right and right - left + 1 - most_count > k:
                cnts[s[left]] -= 1
                # if cnts[s[left]] == most_count - 1:
                #     most_count = max(list(cnts.values()))
                left += 1
            ans = max(ans, right - left + 1)
        return ans
