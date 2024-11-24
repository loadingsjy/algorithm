#
# * 1804. 实现 Trie （前缀树） II - M
# 前缀树（trie ，发音为 "try"）是一个树状的数据结构，用于高效地存储和检索一系列字符串的前缀。前缀树有许多应用，如自动补全和拼写检查。

# 实现前缀树 Trie 类：
# Trie() 初始化前缀树对象。
# void insert(String word) 将字符串 word 插入前缀树中。
# int countWordsEqualTo(String word) 返回前缀树中字符串 word 的实例个数。
# int countWordsStartingWith(String prefix) 返回前缀树中以 prefix 为前缀的字符串个数。
# void erase(String word) 从前缀树中移除字符串 word 。

# 提示：
# 1 <= word.length, prefix.length <= 2000
# word 和 prefix 只包含小写英文字母。
# insert、 countWordsEqualTo、 countWordsStartingWith 和 erase 总共调用最多 3 * 104 次。
# 保证每次调用 erase 时，字符串 word 总是存在于前缀树中。


class TrieNode(object):
    def __init__(self, pass_=0, end=0, next=None):
        self.pass_ = pass_  # 有多少个字符串经过该节点(字母)
        self.end = end  # 以该字母为结尾的字符串个数
        self.next = [None] * 26


class Trie:
    """前缀树：数组实现"""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """将字符串 word 插入前缀树中"""
        cur = self.root
        cur.pass_ += 1
        for ch in word:
            idx = ord(ch) - ord("a")
            if cur.next[idx] is None:
                cur.next[idx] = TrieNode(1, 0)
            else:
                cur.next[idx].pass_ += 1
            cur = cur.next[idx]
        cur.end += 1

    def countWordsEqualTo(self, word: str) -> int:
        """返回前缀树中字符串 word 的实例个数"""
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord("a")
            if cur.next[idx] is None:
                return 0
            else:
                cur = cur.next[idx]
        return cur.end

    def countWordsStartingWith(self, prefix: str) -> int:
        """返回前缀树中以 prefix 为前缀的字符串个数"""
        cur = self.root
        for ch in prefix:
            idx = ord(ch) - ord("a")
            if cur.next[idx] is None:
                return 0
            else:
                cur = cur.next[idx]
        return cur.pass_

    def erase(self, word: str) -> None:
        """从前缀树中移除字符串 word"""
        if self.countWordsEqualTo(word) > 0:
            cur = self.root
            cur.pass_ -= 1
            for ch in word:
                idx = ord(ch) - ord("a")
                if cur.next[idx].pass_ == 1:
                    cur.next[idx] = None
                    return
                else:
                    cur.next[idx].pass_ -= 1
                    cur = cur.next[idx]
            cur.end -= 1


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    # 插入 "apple"。
    trie.insert("apple")
    # 插入另一个 "apple"。
    print(trie.countWordsEqualTo("apple"))
    # 有两个 "apple" 实例，所以返回 2。
    print(trie.countWordsStartingWith("app"))
    # "app" 是 "apple" 的前缀，所以返回 2。
    trie.erase("apple")
    # 移除一个 "apple"。
    print(trie.countWordsEqualTo("apple"))
    # 现在只有一个 "apple" 实例，所以返回 1。
    print(trie.countWordsStartingWith("app"))
    # 返回 1
    trie.erase("apple")
    # 移除 "apple"。现在前缀树是空的。
    print(trie.countWordsStartingWith("app"))
    # 返回 0
