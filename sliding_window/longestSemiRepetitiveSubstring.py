#
# * 2730. 找到最长的半重复子字符串
# 给你一个下标从 0 开始的字符串 s ，这个字符串只包含 0 到 9 的数字字符。
# 如果一个字符串 t 中至多有一对相邻字符是相等的，那么称这个字符串 t 是 半重复的 。例如，"0010" 、"002020" 、"0123" 、"2002" 和 "54944" 是半重复字符串，而 "00101022" （相邻的相同数字对是 00 和 22）和 "1101234883" （相邻的相同数字对是 11 和 88）不是半重复字符串。
# 请你返回 s 中最长 半重复 子字符串的长度。

# 示例 1：
# 输入：s = "52233"
# 输出：4
# 解释：
# 最长的半重复子字符串是 "5223"。整个字符串 "52233" 有两个相邻的相同数字对 22 和 33，但最多只能选取一个。
# 示例 2：
# 输入：s = "5494"
# 输出：4
# 解释：
# s 是一个半重复字符串。
# 示例 3：
# 输入：s = "1111111"
# 输出：2
# 解释：
# 最长的半重复子字符串是 "11"。子字符串 "111" 有两个相邻的相同数字对，但最多允许选取一个。

# 提示：
# 1 <= s.length <= 50
# '0' <= s[i] <= '9'


class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        """滑动窗口"""
        ans, left = 0, 0
        near_count = 0
        for right, ch in enumerate(s):
            if right > 0 and ch == s[right - 1]:
                near_count += 1
            while left < right and near_count > 1:
                if s[left] == s[left + 1]:
                    near_count -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

    def longestSemiRepetitiveSubstring2(self, s: str) -> int:
        """灵神写法"""
        ans, left, same = 1, 0, 0
        for right in range(1, len(s)):
            same += s[right] == s[right - 1]
            if same > 1:
                left += 1
                while s[left] != s[left - 1]:
                    left += 1
                same = 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "52233"
    print(sol.longestSemiRepetitiveSubstring(s))
    print(sol.longestSemiRepetitiveSubstring2(s))

    s = "5494"
    print(sol.longestSemiRepetitiveSubstring(s))
    print(sol.longestSemiRepetitiveSubstring2(s))

    s = "1111111"
    print(sol.longestSemiRepetitiveSubstring(s))
    print(sol.longestSemiRepetitiveSubstring2(s))
