# 839. 相似字符串组

# 如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。
# 例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。
# 总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。
# 给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。请问 strs 中有多少个相似字符串组？

# 示例 1：
# 输入：strs = ["tars","rats","arts","star"]
# 输出：2
# 示例 2：
# 输入：strs = ["omv","ovm"]
# 输出：1

# 提示：
# 1 <= strs.length <= 300
# 1 <= strs[i].length <= 300
# strs[i] 只包含小写字母。
# strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。


class UF:
    """并查集"""

    def __init__(self, n):
        self.father = [i for i in range(n)]
        self.sets = n  # 集合数量

    def find(self, i):
        if i != self.father[i]:
            self.father[i] = self.find(self.father[i])
        return self.father[i]

    def isSameSet(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.father[fx] = fy
            self.sets -= 1


class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        def is_similar(str1, str2):
            """判断两个字符串是否相似"""
            diff = 0
            for ch1, ch2 in zip(str1, str2):
                if ch1 != ch2:
                    diff += 1
                    if diff > 2:
                        return False
            return diff == 0 or diff == 2

        n = len(strs)
        uf = UF(n)
        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    uf.union(i, j)
        return uf.sets


if __name__ == "__main__":
    s = Solution()
    strs = ["tars", "rats", "arts", "star"]
    print(s.numSimilarGroups(strs))
