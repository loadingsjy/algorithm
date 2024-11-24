#
# * 269. 火星词典 - H
# 现有一种使用英语字母的火星语言，这门语言的字母顺序对你来说是未知的。
# 给你一个来自这种外星语言字典的字符串列表 words ，words 中的字符串已经 按这门新语言的字典序进行了排序 。
# 如果这种说法是错误的，并且给出的 words 不能对应任何字母的顺序，则返回 "" 。
# 否则，返回一个按新语言规则的 字典递增顺序 排序的独特字符串。如果有多个解决方案，则返回其中 任意一个 。

# 示例 1：
# 输入：words = ["wrt","wrf","er","ett","rftt"]
# 输出："wertf"
# 示例 2：
# 输入：words = ["z","x"]
# 输出："zx"
# 示例 3：
# 输入：words = ["z","x","z"]
# 输出：""
# 解释：不存在合法字母顺序，因此返回 "" 。

# 提示：
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] 仅由小写英文字母组成

from collections import defaultdict


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        """拓扑排序"""
        n = len(words)
        # if n == 1:
        #     return "".join(list(set(list(words[0]))))

        def str_cmp(str1, str2):
            for ch1, ch2 in zip(str1, str2):
                if ch1 != ch2:
                    return ch1, ch2
            if len(str1) > len(str2):
                return -1, -1
            else:
                return "", ""

        in_degree = dict()
        for word in words:
            for ch in word:
                in_degree[ch] = 0
        next_nodes = defaultdict(list)
        for i in range(1, n):
            ch1, ch2 = str_cmp(words[i - 1], words[i])
            if ch1 == -1:  # word[i]是word[i-1]的严格前缀，肯定不存在答案
                return ""
            if ch1 and ch2:
                next_nodes[ch1].append(ch2)
                in_degree[ch2] += 1

        queue = [ch for ch, d in in_degree.items() if d == 0]

        ans = []
        while queue:
            cur = queue.pop(0)
            ans.append(cur)
            for nxt in next_nodes[cur]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)

        if len(ans) == len(in_degree):
            return "".join(ans)
        else:
            return ""


if __name__ == "__main__":
    sol = Solution()
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print(sol.alienOrder(words))
