# 最长连续公共子串
def lccs(text1: str, text2: str) -> int:

    m, n = len(text1), len(text2)
    # str1[0..i-1]中必须以str1[i-1]结尾 和 str2[0..i-1]中必须以str2[i-1]结尾的 最长公共子串(子串必须包含str1[i-1]/str2[j-1])的长度
    # 这意味着 如果str1[i-1] != str2[j-1]，则dp[i][j] = 0
    # 最后结果就是整张dp表的最大值（不是最后一行/列的最大值）
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
    # print(dp)
    return max([max(l) for l in dp])


# 最长连续公共子串，改进只用一维数组做dp
def lccs_improved(text1: str, text2: str) -> int:

    m, n = len(text1), len(text2)
    dp = [0] * (n + 1)
    max_l = 0
    for i in range(1, m + 1):
        for j in range(n, 0, -1):
            if text1[i - 1] == text2[j - 1]:
                dp[j] = dp[j - 1] + 1
            else:
                dp[j] = 0
        max_l = max(max_l, max(dp))
        # print(dp)
    return max_l


# 最长连续公共子串，改进只用几个变量做dp
def lccs_improved_v2(text1: str, text2: str) -> int:

    m, n = len(text1), len(text2)
    max_l = 0
    row = 0
    col = n - 1

    end = -1
    while row < m:
        i = row
        j = col
        length = 0
        while i < m and j < n:
            if text1[i] != text2[j]:
                length = 0
            else:
                length += 1
            if length > max_l:
                max_l = length
                end = i
            # 斜对角线
            i += 1
            j += 1
        # 从右向左，从上向下
        if col > 0:
            col -= 1
        else:
            row += 1
    print("最长连续公共子串: ", text1[end - max_l + 1 : end + 1])
    return max_l
