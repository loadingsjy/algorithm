#
# * 127. 单词接龙 - H
# 字典 wordList 中从单词 beginWord 到 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 -> s2 -> ... -> sk：
# 每一对相邻的单词只差一个字母。
#  对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
# sk == endWord
# 给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0 。

# 示例 1：
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# 输出：5
# 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
# 示例 2：
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# 输出：0
# 解释：endWord "cog" 不在字典中，所以无法进行转换。

# 提示：
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord、endWord 和 wordList[i] 由小写英文字母组成
# beginWord != endWord
# wordList 中的所有字符串 互不相同


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        """双向广搜"""
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        smallLevel = set()  #  数量小的一侧
        smallLevel.add(beginWord)

        bigLevel = set()  # 数量大的一侧
        bigLevel.add(endWord)

        nextLevel = set()  # 由数量小的一侧，所扩展出的下一层列表

        level = 2
        while smallLevel:
            # 从数量小的那侧进行 bfs
            for word in smallLevel:
                word_l = list(word)
                for i in range(len(word)):
                    # 对字符串的每个位置进行替换，看它在不在word_set集合中，如果在word_set集合中，就加入nextLevel
                    # 不要遍历word_set每个单词，与word进行对比相差一个字符，就加入nextLevel，这样遍历复杂度高
                    old = word_l[i]
                    for k in range(26):
                        new = chr(ord("a") + k)
                        if new == old:
                            continue
                        word_l[i] = new
                        next_word = "".join(word_l)
                        if next_word in bigLevel:
                            return level
                        if next_word in word_set:
                            nextLevel.add(next_word)
                            word_set.remove(next_word)
                    word_l[i] = old  # 还原

            if len(nextLevel) > len(bigLevel):
                nextLevel, bigLevel = bigLevel, nextLevel
            smallLevel = nextLevel
            nextLevel = set()
            level += 1

        return 0


if __name__ == "__main__":
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(sol.ladderLength(beginWord, endWord, wordList))
