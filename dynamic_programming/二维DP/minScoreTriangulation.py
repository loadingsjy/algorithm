# 你有一个凸的 n 边形，其每个顶点都有一个整数值。给定一个整数数组 values ，其中 values[i] 是第 i 个顶点的值（即 顺时针顺序 ）。
# 假设将多边形 剖分 为 n - 2 个三角形。对于每个三角形，该三角形的值是顶点标记的乘积，三角剖分的分数是进行三角剖分后所有 n - 2 个三角形的值之和。
# 返回 多边形进行三角剖分后可以得到的最低分 。

# 示例：
# 输入：values = [3,7,4,5]
# 输出：144
# 解释：有两种三角剖分，可能得分分别为：3*7*5 + 4*5*7 = 245，或 3*4*5 + 3*4*7 = 144。最低分数为 144。

from functools import cache


class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:

        n = len(values)

        @cache
        def dfs(i, j):
            if i + 1 == j:
                return 0
            res = float("inf")
            for k in range(i + 1, j):
                res = min(res, dfs(i, k) + dfs(k, j) + values[i] * values[j] * values[k])
            return res

        return dfs(0, n - 1)

    def minScoreTriangulation_dp(self, values: list[int]) -> int:

        n = len(values)

        dp = [[0] * n for _ in range(n)]

        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                res = float("inf")
                for k in range(i + 1, j):
                    res = min(res, dp[i][k] + dp[k][j] + values[i] * values[j] * values[k])
                dp[i][j] = res

        return dp[0][n-1]
    
    
if __name__ == '__main__':
    s = Solution()
    
    values = [3,7,4,5]
    print(s.minScoreTriangulation(values))
    print(s.minScoreTriangulation_dp(values))


    values = [1,3,1,4,1,5]
    print(s.minScoreTriangulation_dp(values))
    print(s.minScoreTriangulation_dp(values))

