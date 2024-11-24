# 给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。

# 示例 1:
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


from collections import Counter


# 滑动窗口
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if n <= 1:
        return n
    # 哈希集合，记录每个字符是否出现过
    occ = set()
    max_len = 0
    left = 0
    while left < n - 1:
        occ.add(s[left])
        right = left + 1
        while right < n:
            # 如果是不重复元素，则右指针右移
            if s[right] not in occ:
                occ.add(s[right])
                right += 1
            # 如果有重复元素，左指针右移，并去掉当前左指针元素
            else:
                occ.remove(s[left])
                max_len = max(max_len, right - left)
                left += 1
        # 最后一个不重复子串的长度
        max_len = max(max_len, right - left)

    return max_len


def lengthOfLongestSubstring2(s: str) -> int:
    # 哈希集合，记录每个字符是否出现过
    occ = set()
    n = len(s)
    # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
    right, ans = -1, 0
    for left in range(n):
        if left != 0:
            # 左指针向右移动一格，移除一个字符
            occ.remove(s[left - 1])
        while right + 1 < n and s[right + 1] not in occ:
            # 不断地移动右指针
            occ.add(s[right + 1])
            right += 1
        # 第 left 到 right 个字符是一个极长的无重复字符子串
        ans = max(ans, right - left + 1)
    return ans


# 滑动窗口
def lengthOfLongestSubstring3(s: str) -> int:
    left, ans = 0, 0
    occ = []

    for right, c in enumerate(s):  # 移动子串右端点
        occ.append(c)  # 右端点字母移入子串
        while left <= right and len(occ) > len(set(occ)):  # 有重复元素
            occ.pop(0)  # 左端点字母移出子串
            left += 1  # 移动子串左端点
        ans = max(ans, right - left + 1)
    return ans


# 动态规划
def lengthOfLongestSubstring_dp(s: str) -> int:
    if not s:
        return 0
    n = len(s)
    last_char_index = [-1] * 256  # 记录上一次出现该字符的位置
    pre = -1
    max_len = 0
    for i in range(n):
        # 上一次出现该字符的位置、以i-1结尾的最长无重复子串的起始位置， 两者取靠右的位置
        pre = max(pre, last_char_index[ord(s[i])])
        max_len = max(max_len, i - pre)
        last_char_index[ord(s[i])] = i
    return max_len


if __name__ == "__main__":

    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))
    print(lengthOfLongestSubstring2(s))
    print(lengthOfLongestSubstring3(s))
    print(lengthOfLongestSubstring_dp(s))
    print()

    s = "bbbbb"
    print(lengthOfLongestSubstring(s))
    print(lengthOfLongestSubstring2(s))
    print(lengthOfLongestSubstring3(s))
    print(lengthOfLongestSubstring_dp(s))
    print()

    s = "pwwkew"
    print(lengthOfLongestSubstring(s))
    print(lengthOfLongestSubstring2(s))
    print(lengthOfLongestSubstring3(s))
    print(lengthOfLongestSubstring_dp(s))
