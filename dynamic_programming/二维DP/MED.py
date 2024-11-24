# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符

# 示例 1：
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')

# 示例 2：
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (插入 'u')
# exection -> execution (插入 'n')

# 提示：
# 0 <= word1.length, word2.length <= 500
# word1 和 word2 由小写英文字母组成


# 最小编辑距离
def minEidtDistance(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])    # 删除，插入，替换
    return dp[n][m]


if __name__ == '__main__':
    word1 = "horse" 
    word2 = "ros"
    print(minEidtDistance(word1, word2)) # 3

    word1 = "intention" 
    word2 = "execution"
    print(minEidtDistance(word1, word2)) # 5