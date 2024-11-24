#
# * 1657. 确定两个字符串是否接近
# 如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 接近 ：
# 操作 1：交换任意两个 现有 字符。
# 例如，abcde -> aecdb
# 操作 2：将一个 现有 字符的每次出现转换为另一个 现有 字符，并对另一个字符执行相同的操作。
# 例如，aacabb -> bbcbaa（所有 a 转化为 b ，而所有的 b 转换为 a ）
# 你可以根据需要对任意一个字符串多次使用这两种操作。
# 给你两个字符串，word1 和 word2 。如果 word1 和 word2 接近 ，就返回 true ；否则，返回 false 。

# 示例 1：
# 输入：word1 = "abc", word2 = "bca"
# 输出：true
# 解释：2 次操作从 word1 获得 word2 。
# 执行操作 1："abc" -> "acb"
# 执行操作 1："acb" -> "bca"
# 示例 2：
# 输入：word1 = "a", word2 = "aa"
# 输出：false
# 解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。
# 示例 3：
# 输入：word1 = "cabbba", word2 = "abbccc"
# 输出：true
# 解释：3 次操作从 word1 获得 word2 。
# 执行操作 1："cabbba" -> "caabbb"
# 执行操作 2："caabbb" -> "baaccc"
# 执行操作 2："baaccc" -> "abbccc"
# 提示：
# 1 <= word1.length, word2.length <= 105
# word1 和 word2 仅包含小写英文字母


from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        判断 s 和 t 的长度是否一样，如果不一样直接返回 false。
        判断 s 和 t 的字符集合是否一样，如果不一样直接返回 false。例如 s 中有字符 abc，t 中有字符 def，我们无论如何都不能把 s 变成 t。
        判断 s 的字符出现次数的集合，是否等于 t 的字符出现次数的集合，等于返回 true，不等于返回 false。注意集合可以有相同元素，比如 aabbbccc 对应的集合就是 {2,3,3}。
        """
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        return (
            len(word1) == len(word2)
            and set(word1) == set(word2)
            and Counter(cnt1.values()) == Counter(cnt2.values())
        )


if __name__ == "__main__":
    sol = Solution()
    word1 = "cabbba"
    word2 = "abbccc"
    print(sol.closeStrings(word1, word2))