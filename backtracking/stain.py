# 给定一个任意颜色序列，要求对每个位置进行染色，要求绿色Green的左边没有红色Red，红色的右边没有绿色，求染色数量最少的方案。


# 暴力法，对每个loc(loc:0~n)统计左边需要染成绿色的个数，右边需要染成红色的个数，然后求和，最后取和的最小值。
# 时间复杂度O(n^2)

# 优化，设计两个数组，left[i]表示第0-i-1个位置左边非绿色的个数，right[i]表示第i-n个位置右边非红色的个数。
# 时间复杂度O(n)

def MinStain(colors):
    n = len(colors)
    dp = [0] * n
    for i in range(n):
        if colors[i] == 'R':
            dp[i] = 1
        else:
            for j in range(i):
                if colors[j] == 'R':
                    dp[i] += 1
    ans = float('inf')
    for i in range(n):
        if colors[i] == 'G':
            for j in range(i+1, n):
                if colors[j] == 'R':
                    ans = min(ans, dp[i] + dp[j])
    return ans

if __name__ == '__main__':
    colors = ['R', 'G', 'G', 'R', 'R', 'G']
    print(MinStain(colors))  # Output: 2