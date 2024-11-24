class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        haystack_length = len(haystack)
        needle_length = len(needle)
        return self.bm(haystack, haystack_length, needle, needle_length)

    # 实现 Boyer-Moore 算法
    def bm(self, s, s_len, t, t_len):
        # 获取好后缀移动位数表
        bc_dict = self.badChar(t, t_len)
        # suffix 用来保存各种长度好后缀的最右位置的数组
        # prefix 判断是否是头部，如果是头部则true
        suffix, prefix = self.goodSuffix(t, t_len)
        # 用来存储已经查询过的好后缀移动位数，可减少时间开销（优化点）
        gs_dict = [None] * t_len
        # 第一个匹配字符
        now = 0
        # 如果匹配字符的位置到达两字符长度的差值，则不可能存在匹配字串，则退出循环
        while now <= s_len - t_len:
            i = t_len - 1
            # 从后往前匹配，匹配失败，找到坏字符
            while i >= 0 and s[now + i] == t[i]:
                i -= 1
            # 退出条件，模式串遍历完毕，匹配成功，返回当前下标 now
            if i < 0:
                return now
            # 下面为匹配失败时，如何处理
            # 求出坏字符规则下移动的位数，就是我们坏字符下标减最右边的下标
            bc_move = i - bc_dict.get(s[now + i], -1)
            gs_move = 0
            # 好后缀情况，求出好后缀情况下的移动位数,如果不含有好后缀的话，则按照坏字符来
            if t_len - 1 > 0 and t_len - 1 > i:
                # 判断是否计算过，如果没有计算过则需要计算后存储答案至列表
                if gs_dict[i] is None:
                    gs_dict[i] = self.move(i, t_len, suffix, prefix)
                gs_move = gs_dict[i]
            # 选择最大偏移位数进行移动
            now += max(bc_move, gs_move)
        return -1

    # 根据 suffix 和 prefix 以及坏字符的下标获取到好后缀的移动位数
    def move(self, i, t_len, suffix, prefix):
        # i代表坏字符的下标
        # 好后缀长度
        suffix_length = t_len - 1 - i
        # 如果含有长度为 suffix_length 的好后缀，返回移动位数
        if suffix[suffix_length] != -1:
            return i + 1 - suffix[suffix_length]
        # 找头部为好后缀子串的最大长度，从长度最大的子串开始
        for k in range(suffix_length - 1, 0, -1):
            # 如果是头部，则移动 t_len - k 个位数
            if prefix[k] is True:
                return t_len - k
        # 如果没有发现 好后缀匹配的串/头部为好后缀子串，则移动到 t_len 位，也就是模式串的长度
        return t_len

    # 用来求坏字符情况下移动位数
    def badChar(self, t, t_len):
        # 初始化
        bc_dict = dict()
        # t_len 代表模式串的长度，如果有两个字符'a',则后面那个会覆盖前面那个的位置
        # 因此可以保证最终得到的是字符在模式串中的最后一个位置
        for i in range(t_len):
            bc_dict[t[i]] = i
        return bc_dict

    # 用来求辅助数组 suffix 和 prefix
    def goodSuffix(self, t, t_len):
        # 初始化
        suffix = [-1] * t_len
        prefix = [False] * t_len
        # 递增子串长度，直到 t_len-1，从 0 开始可以从远到近依次覆盖得到最优 suffix
        for i in range(t_len - 1):
            start = i
            suffix_length = 0
            # 更新 suffix 数组，分别从取子串和模式串倒数第一个值开始
            # 如果相等且子串长度不为 0，则令 suffix[suffix_length] = start，
            # 其中suffix_length为后缀长度，start 等同于模式串中与后缀相同的字符串所处的位置
            while start >= 0 and t[start] == t[t_len - 1 - suffix_length]:
                suffix_length += 1
                suffix[suffix_length] = start
                start -= 1
            # 更新prefix数组，等于-1说明已经遍历完字符串头部
            if start == -1:
                prefix[suffix_length] = True
        return suffix, prefix


if __name__ == "__main__":
    s = Solution()
    print(s.strStr("hello", "ll"))

    print(s.strStr("aaaaa", "bba"))

    print(s.strStr("mississippi", "issip"))

    print(s.strStr("ABABDABACDABABCABAB", "ABCABAB"))

    print(s.strStr("aabaabaafaabaabaaf", "aabaa"))
