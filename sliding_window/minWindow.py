from collections import defaultdict

# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 注意：
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。

# 示例 1：
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
# 示例 2：
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
# 示例 3:
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。


from collections import Counter


# s 中是否涵盖 t 所有字符
def match(s: str, t: str) -> bool:
    count = defaultdict(int)
    for c in t:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    for c in s:
        if c in count:
            count[c] -= 1
            if count[c] == 0:
                del count[c]
        if not count:
            return True
    return False


def minWindow(s: str, t: str) -> str:
    left, right = 0, len(t) - 1
    min_len = float("inf")  # 最小子串长度
    min_start = 0  # 最小子串起始位置
    while right < len(s) and left <= right:
        if match(s[left : right + 1], t):
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            left += 1
        else:
            right += 1
    if min_len == float("inf"):
        return ""
    else:
        return s[min_start : min_start + min_len]


def minWindow2(s: str, t: str) -> str:
    """时间复杂度：O(∣Σ∣m+n)，其中 m 为 s 的长度，n 为 t 的长度，∣Σ∣ 为字符集合的大小，本题字符均为英文字母，所以 ∣Σ∣=52。
    注意 left 只会增加不会减少，left 每增加一次，我们就花费 O(∣Σ∣) 的时间。
    因为 left 至多增加 m 次，所以二重循环的时间复杂度为 O(∣Σ∣m)，再算上统计 t 字母出现次数的时间 O(n)，总的时间复杂度为 O(∣Σ∣m+n)。
    空间复杂度：O(∣Σ∣)。如果创建了大小为 128 的数组，则 ∣Σ∣=128。"""
    ans_left, ans_right = -1, len(s)
    left = 0
    cnt_s = Counter()  # s 子串字母的出现次数
    cnt_t = Counter(t)  # t 中字母的出现次数

    for right, c in enumerate(s):  # 移动子串右端点
        cnt_s[c] += 1  # 右端点字母移入子串
        while cnt_s >= cnt_t:  # 涵盖
            if right - left < ans_right - ans_left:  # 找到更短的子串
                ans_left, ans_right = left, right  # 记录此时的左右端点
            cnt_s[s[left]] -= 1  # 左端点字母移出子串
            left += 1  # 移动子串左端点
    return "" if ans_left < 0 else s[ans_left : ans_right + 1]


def minWindow3(s: str, t: str) -> str:

    ans_left, ans_right = -1, len(s)
    left = 0
    cnt_s = Counter()  # s 子串字母的出现次数
    cnt_t = Counter(t)  # t 中字母的出现次数
    less = len(cnt_t)  # 有 less 种字母的出现次数 < t 中的字母出现次数

    for right, c in enumerate(s):  # 移动子串右端点
        cnt_s[c] += 1  # 右端点字母移入子串
        if cnt_s[c] == cnt_t[c]:
            less -= 1  # c 的出现次数从 < 变成 >=
        while less == 0:  # 涵盖：所有字母的出现次数都是 >=
            if right - left < ans_right - ans_left:  # 找到更短的子串
                ans_left, ans_right = left, right  # 记录此时的左右端点
            x = s[left]  # 左端点字母
            if cnt_s[x] == cnt_t[x]:
                less += 1  # x 的出现次数从 >= 变成 <（下一行代码执行后）
            cnt_s[x] -= 1  # 左端点字母移出子串
            left += 1  # 移动子串左端点
    return "" if ans_left < 0 else s[ans_left : ans_right + 1]


# 时间复杂度：O(m+n) 或 O(m+n+∣Σ∣)，其中 m 为 s 的长度，n 为 t 的长度，∣Σ∣=128。
# 注意 left 只会增加不会减少，二重循环的时间复杂度为 O(m)。
# 使用哈希表写法的时间复杂度为 O(m+n)，数组写法的时间复杂度为 O(m+n+∣Σ∣)。
# 空间复杂度：O(∣Σ∣)。无论 m 和 n 有多大，额外空间都不会超过 O(∣Σ∣)。


if __name__ == "__main__":
    # test
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s, t))  # output: "BANC"
    print(minWindow2(s, t))
    print(minWindow3(s, t))
    print()

    s = "a"
    t = "a"
    print(minWindow(s, t))  # output: "a"
    print(minWindow2(s, t))
    print(minWindow3(s, t))
    print()

    # s = "a"
    # t = "aa"
    # print(minWindow(s, t))  # output: ""
    # print(minWindow2(s, t))
    # print(minWindow2_2(s, t))
    # print(minWindow3(s, t))
    # print()

    s = "ADOBECODEABADNC"
    t = "ABCD"
    print(minWindow(s, t))
    print(minWindow2(s, t))
    print(minWindow3(s, t))
    print()
