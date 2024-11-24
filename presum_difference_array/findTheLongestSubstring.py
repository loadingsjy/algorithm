#
# * 1371. 每个元音包含偶数次的最长子字符串

# 给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

# 示例 1：
# 输入：s = "eleetminicoworoep"
# 输出：13
# 解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
# 示例 2：
# 输入：s = "leetcodeisgreat"
# 输出：5
# 解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
# 示例 3：
# 输入：s = "bcbcbc"
# 输出：6
# 解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。

# 提示：
# 1 <= s.length <= 5 x 10^5
# s 只包含小写英文字母。


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """前缀和 + 状态压缩"""
        char_map = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        # i表示前缀元音字母奇偶性状态，共5个状态位，所以一共有32个状态，
        # mp[i]表示 前缀元音字母奇偶性状态 最早出现的位置，-2代表没有出现过
        mp = [-2] * 32
        mp[0] = -1
        pre_status = 0  # 元音字母状态（只使用5个状态位），0为偶数次，1为奇数次
        ans = 0

        for i, ch in enumerate(s):
            if ch in char_map:  # 是元音字母，改变状态位
                pre_status ^= 1 << char_map[ch]
            if mp[pre_status] != -2:
                ans = max(ans, i - mp[pre_status])
            else:
                mp[pre_status] = i
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "eleetminicoworoep"
    print(sol.findTheLongestSubstring(s))

    s = "leetcodeisgreat"
    print(sol.findTheLongestSubstring(s))

    s = "bcbcbc"
    print(sol.findTheLongestSubstring(s))
