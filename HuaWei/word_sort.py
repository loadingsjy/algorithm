# 给定字符串s,s包括以空格分割若干个单词，请对s进行如下处理后输出：
# 1.单词内部调整：对每个单词字母重新按字典序排序
# 2.单词间顺序调整
# 1)统计每个单词出现的次数，并按次数降序排序
# 2)次数相同,按照单词长度升序排序
# 3)次数和单词长度均相同，按字典升序排序
# 请输出处理后的字符串，每个单词以一个空格分割

from collections import defaultdict
import sys


class word(object):
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            if len(self.word) == len(other.word):
                return self.word < other.word
            else:
                return len(self.word) < len(other.word)
        else:
            return self.freq > other.freq


def word_sort(s):
    words_dict = defaultdict(int)
    for i in range(len(s)):
        s[i] = "".join(sorted(list(s[i])))
        words_dict[s[i]] += 1

    words_list = [word(k, v) for k, v in words_dict.items()]
    words_list.sort()
    res = []
    for w in words_list:
        res += [w.word] * w.freq
    # print(' '.join(res))
    return res


if __name__ == "__main__":
    for line in sys.stdin:
        # if not line.strip:
        #     break
        a = str(line.strip())
        break
    words = list(a.split())
    res = word_sort(words)
    print(" ".join(res))
