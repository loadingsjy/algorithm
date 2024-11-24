#
# * 940. 不同的子序列 II - H
# 给定一个字符串 s，计算 s 的 不同非空子序列 的个数。因为结果可能很大，所以返回答案需要对 10^9 + 7 取余 。
# 字符串的 子序列 是经由原字符串删除一些（也可能不删除）字符但不改变剩余字符相对位置的一个新字符串。
# 例如，"ace" 是 "abcde" 的一个子序列，但 "aec" 不是。

# 示例 1：
# 输入：s = "abc"
# 输出：7
# 解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。
# 示例 2：
# 输入：s = "aba"
# 输出：6
# 解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。
# 示例 3：
# 输入：s = "aaa"
# 输出：3
# 解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。

# 提示：
# 1 <= s.length <= 2000
# s 仅由小写英文字母组成

from collections import defaultdict

MOD = 10**9 + 7


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        '''"""把原问题细分一下，改为分别统计以 ‘a’,‘b’,⋯,‘z’ 结尾的不同子序列的个数
        你也可以这样理解：这种做法对于相同的子序列，只会考虑其最后一次出现的位置（下标序列的字典序最大）。"""'''
        cnt = defaultdict(int)
        total, new_add = 1, 0
        for ch in s:  # 每次新增以ch为结尾的子序列数量（不能重复计算）
            new_add = total - cnt[ch]  # 纯新增 的 以ch为结尾的子序列数量
            cnt[ch] = cnt[ch] + new_add
            total = (total + new_add) % MOD
        return (total - 1 + MOD) % MOD


if __name__ == "__main__":
    sol = Solution()
    s = "aba"
    print(sol.distinctSubseqII(s))
