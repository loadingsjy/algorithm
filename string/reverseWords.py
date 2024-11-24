# 给你一个字符串 s ，请你反转字符串中 单词 的顺序。
# 单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
# 返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
# 注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

# 示例 1：
# 输入：s = "the sky is blue"
# 输出："blue is sky the"
# 示例 2：
# 输入：s = "  hello world  "
# 输出："world hello"
# 解释：反转后的字符串中不能存在前导空格和尾随空格。
# 示例 3：
# 输入：s = "a good   example"
# 输出："example good a"
# 解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。


# 倒序遍历字符串 s ，记录单词左右索引边界 i , j 。
# 每确定一个单词的边界，则将其添加至单词列表 res 。
# 最终，将单词列表拼接为字符串，并返回即可。


# 一、双指针（倒序遍历 + 分割）不需要删除头尾多余的空格
def reverseWords(s: str) -> str:
    # s = s.strip()
    result = []
    n = len(s)
    i = n
    j = i - 1
    while i > j and j != 0:
        for j in range(i - 1, -1, -1):
            if s[j] == " ":
                if i != j + 1:
                    result.append(s[j + 1 : i])
                    i = j
                else:  # 连续空格
                    i -= 1
    if s[j] != " ":
        result.append(s[j:i])
    return " ".join(result)


def reverseWords2(s: str) -> str:
    return " ".join(reversed(s.split()))


if __name__ == "__main__":
    s = "the sky is blue"
    print(reverseWords(s))
    print(reverseWords2(s))

    s = "  hello world  "
    print(reverseWords(s))
    print(reverseWords2(s))

    s = "  a good   example"
    print(reverseWords(s))
    print(reverseWords2(s))
