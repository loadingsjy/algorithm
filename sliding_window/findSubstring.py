from collections import Counter

# 给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。
#  s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。
# 例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
# 返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。

# 示例 1：
# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
# 子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
# 子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
# 输出顺序无关紧要。返回 [9,0] 也是可以的。

# 示例 2：
# 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# 输出：[]
# 解释：因为 words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。
# s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。
# 所以我们返回一个空数组。

# 示例 3：
# 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# 输出：[6,9,12]
# 解释：因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。
# 子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。
# 子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。
# 子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。


def findSubstring(s: str, words: list[str]) -> list[int]:
    res = []
    m, n, ls = len(words), len(words[0]), len(s)
    for i in range(n):
        if i + m * n > ls:
            break
        differ = Counter()
        for j in range(m):
            word = s[i + j * n : i + (j + 1) * n]
            differ[word] += 1
        for word in words:
            differ[word] -= 1
            if differ[word] == 0:
                del differ[word]
        for start in range(i, ls - m * n + 1, n):
            if start != i:
                word = s[start + (m - 1) * n : start + m * n]
                differ[word] += 1
                if differ[word] == 0:
                    del differ[word]
                word = s[start - n : start]
                differ[word] -= 1
                if differ[word] == 0:
                    del differ[word]
            if len(differ) == 0:
                res.append(start)
    return res


s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words))  # [9, 0]

s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
print(findSubstring(s, words))  # []

s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
print(findSubstring(s, words))  # [6, 9, 12]
