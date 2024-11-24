from collections import Counter

# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

# 示例 1:
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#  示例 2:
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。


def is_Ectopic(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_c = Counter(s1)
    s2_c = Counter(s2)
    if s1_c == s2_c:
        return True
    else:
        return False


# 方法超时
def findAnagrams(s: str, p: str) -> list[int]:
    p_counter = Counter(p)
    n = len(p)
    res = []
    for i in range(len(s) - n + 1):
        window_counter = Counter(s[i : i + n])
        if window_counter == p_counter:
            res.append(i)
    return res


# 根据题目要求，我们需要在字符串 s 寻找字符串 p 的异位词。因为字符串 p 的异位词的长度一定与字符串 p 的长度相同，
# 所以我们可以在字符串 s 中构造一个长度为与字符串 p 的长度相同的滑动窗口，并在滑动中维护窗口中每种字母的数量；
# 当窗口中每种字母的数量与字符串 p 中每种字母的数量相同时，则说明当前窗口为字符串 p 的异位词。


def findAnagrams_v2(s: str, p: str) -> list[int]:
    """时间复杂度：O(m+(n−m)×Σ)，其中 n 为字符串 s 的长度，m 为字符串 p 的长度，Σ 为所有可能的字符数。
    我们需要 O(m) 来统计字符串 p 中每种字母的数量；需要 O(m) 来初始化滑动窗口；
    需要判断 n−m+1 个滑动窗口中每种字母的数量是否与字符串 p 中每种字母的数量相同，每次判断需要 O(Σ) 。
    因为 s 和 p 仅包含小写字母，所以 Σ=26。
    空间复杂度：O(Σ)。用于存储字符串 p 和滑动窗口中每种字母的数量。"""

    s_len, p_len = len(s), len(p)
    if s_len < p_len:
        return []
    ans = []
    s_count = [0] * 26
    p_count = [0] * 26
    ord_a = ord("a")
    for i in range(p_len):
        s_count[ord(s[i]) - ord_a] += 1
        p_count[ord(p[i]) - ord_a] += 1

    if s_count == p_count:
        ans.append(0)

    for i in range(s_len - p_len):
        s_count[ord(s[i]) - ord_a] -= 1
        s_count[ord(s[i + p_len]) - ord_a] += 1
        if s_count == p_count:
            ans.append(i + 1)

    return ans


def findAnagrams_v3(s: str, p: str) -> list[int]:
    """时间复杂度：O(n+m+Σ)，其中 n 为字符串 s 的长度，m 为字符串 p 的长度，其中Σ 为所有可能的字符数。
    我们需要 O(m) 来统计字符串 p 中每种字母的数量；需要 O(m) 来初始化滑动窗口；需要 O(Σ) 来初始化 differ；
    需要 O(n−m) 来滑动窗口并判断窗口内每种字母的数量是否与字符串 p 中每种字母的数量相同，每次判断需要 O(1) 。
    因为 s 和 p 仅包含小写字母，所以 Σ=26。
    空间复杂度：O(Σ)。用于存储滑动窗口和字符串 p 中每种字母数量的差。"""

    s_len, p_len = len(s), len(p)

    if s_len < p_len:
        return []

    ans = []
    count = [0] * 26
    for i in range(p_len):
        count[ord(s[i]) - 97] += 1
        count[ord(p[i]) - 97] -= 1

    # 求s和p中不同字符的数量
    differ = [c != 0 for c in count].count(True)

    if differ == 0:
        ans.append(0)

    for i in range(s_len - p_len):
        # 窗口中字母 s[i] 的数量与字符串 p 中的数量从不同变得相同
        if count[ord(s[i]) - 97] == 1:
            differ -= 1
        # 窗口中字母 s[i] 的数量与字符串 p 中的数量从相同变得不同
        elif count[ord(s[i]) - 97] == 0:
            differ += 1

        count[ord(s[i]) - 97] -= 1

        # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从不同变得相同
        if count[ord(s[i + p_len]) - 97] == -1:
            differ -= 1
        # 窗口中字母 s[i+p_len] 的数量与字符串 p 中的数量从相同变得不同
        elif count[ord(s[i + p_len]) - 97] == 0:
            differ += 1

        count[ord(s[i + p_len]) - 97] += 1

        if differ == 0:
            ans.append(i + 1)

    return ans


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(findAnagrams(s, p))
    print(findAnagrams_v2(s, p))
    print(findAnagrams_v3(s, p))

    s = "abab"
    p = "ab"
    print(findAnagrams(s, p))
    print(findAnagrams_v2(s, p))
    print(findAnagrams_v3(s, p))
