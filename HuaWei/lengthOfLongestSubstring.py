# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串  的长度。
# 需要考虑计算复杂度。
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


def maxLength(s):
    """由于左右指针最多移动n次，所以时间复杂度O(N)，空间复杂度O(1)"""
    if not s:
        return 0

    occ = set()  # 记录在窗口内的字符
    n = len(s)
    right = -1
    ans = 0  # 答案
    for left in range(n):
        # 右指针不断右移，直到出现重复字符为止
        while right + 1 < n and s[right + 1] not in occ:
            occ.add(s[right + 1])
            right += 1
        # 更新答案
        ans = max(ans, right - left + 1)
        # 对应for循环：左指针不断左移，直到不出现重复字符为止
        occ.remove(s[left])

    return ans


if __name__ == "__main__":
    s = "abcabcbb"
    print(maxLength(s))
    s = "bbbbb"
    print(maxLength(s))
    s = "pwwkew"
    print(maxLength(s))
