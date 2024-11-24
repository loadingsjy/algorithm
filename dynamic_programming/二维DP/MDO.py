#给定两个字符串 s1 和 s2，我们需要计算在 s1和s2 中删除字符使得 s1 变成 s2 的最小操作数。
# count_minium_delete_operations

def mdo(s1: str, s2: str) -> int:
    m = len(s1)
    n = len(s2)
    
    # dp[i][j] 表示 s1[:i] 和 s2[:j] 之间的最小删除操作数
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 2)

    return dp[m][n]


# 另外一种思路：先算出s1和s2的最长公共子序列的长度lcs，最后用len(s1)+len(s2)-2*lcs得到需要最小的删除操作数。

if __name__ == '__main__':
    s1 = "adcbe"
    s2 = "bcad"
    print(mdo(s1, s2))