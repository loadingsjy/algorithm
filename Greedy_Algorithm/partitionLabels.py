# 给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。

# 注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。

# 返回一个表示每个字符串片段的长度的列表。


# 示例 1：
# 输入：s = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。
# 示例 2：

# 输入：s = "eccbbbbdec"
# 输出：[10]


def partitionLabels(s: str) -> list[int]:
    last_index = {c: i for i, c in enumerate(s)}  # 记录每个字符在字符串中最后出现的位置
    result = []
    start = 0
    end = 0
    for i, c in enumerate(s):
        end = max(last_index[c], end)  # 更新字符最后出现的位置
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result


if __name__ == "__main__":

    s = "ababcbacadefegdehijhklij"
    print(partitionLabels(s))  # [9, 7, 8]

    s = "eccbbbbdec"
    print(partitionLabels(s))  # [10]
