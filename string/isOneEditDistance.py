#
# * 161. 相隔为 1 的编辑距离 - M

# 给定两个字符串 s 和 t ，如果它们的编辑距离为 1 ，则返回 true ，否则返回 false 。
# 字符串 s 和字符串 t 之间满足编辑距离等于 1 有三种可能的情形：
# 1.往 s 中插入 恰好一个 字符得到 t
# 2.从 s 中删除 恰好一个 字符得到 t
# 3.在 s 中用 一个不同的字符 替换 恰好一个 字符得到 t

# 示例 1：
# 输入: s = "ab", t = "acb"
# 输出: true
# 解释: 可以将 'c' 插入字符串 s 来得到 t。
# 示例 2:
# 输入: s = "cab", t = "ad"
# 输出: false
# 解释: 无法通过 1 步操作使 s 变为 t。

# 提示:
# 0 <= s.length, t.length <= 104
# s 和 t 由小写字母，大写字母和数字组成


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """双指针"""
        if len(s) > len(t):
            s, t = t, s
        n = len(s)
        m = len(t)
        if m - n >= 2:
            return False
        # if n == m:
        #     return sum([ch1 != ch2 for ch1, ch2 in zip(s, t)]) == 1
        for i in range(n):
            if s[i] != t[i]:
                if n != m:
                    return s[i:] == t[i + 1 :]
                else:
                    return s[i + 1 :] == t[i + 1 :]
        return n + 1 == m

    def isOneEditDistance2(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False

        i = 0
        while i < len(s) and i < len(t):
            if s[i] != t[i]:
                insert = s[i:] == t[i + 1 :]
                delete = s[i + 1 :] == t[i:]
                replace = s[i + 1 :] == t[i + 1 :]
                if insert or delete or replace:
                    return True
                else:
                    return False
            i += 1

        return True


if __name__ == "__main__":
    sol = Solution()
    s = "ab"
    t = "acb"
    print(sol.isOneEditDistance(s, t))
    print(sol.isOneEditDistance2(s, t))
