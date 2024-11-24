#
# * 345. 反转字符串中的元音字母 - E
# 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
# 元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。

# 示例 1：
# 输入：s = "IceCreAm"
# 输出："AceCreIm"
# 解释：
# s 中的元音是 ['I', 'e', 'e', 'A']。反转这些元音，s 变为 "AceCreIm".
# 示例 2：
# 输入：s = "leetcode"
# 输出："leotcede"

# 提示：
# 1 <= s.length <= 3 * 105
# s 由 可打印的 ASCII 字符组成


class Solution:
    def reverseVowels(self, s: str) -> str:
        """双指针"""
        s = list(s)
        Vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            while i < j and s[i] not in Vowel_set:
                i += 1
            while i < j and s[j] not in Vowel_set:
                j -= 1
            if i < j and s[i] in Vowel_set and s[j] in Vowel_set:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            else:
                break
        return "".join(s)


if __name__ == "__main__":
    sol = Solution()
    s = "IceCreAm"
    print(sol.reverseVowels(s))
