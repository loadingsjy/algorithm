from functools import cache
from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """我们需要在递归过程中，知道当前切的这根棍子，左端点在哪，右端点在哪。
        因此，定义状态为 dfs(i,j)，表示切割一根左端点为 cuts[i]，右端点为 cuts[j] 的棍子的最小成本。
        枚举在 cuts[k] 处切一刀，其中 k=i+1,i+2,…,j−1，木棍变成两段：

        第一段左端点为 cuts[i]，右端点为 cuts[k]，切割这段木棍的最小成本为 dfs(i,k)。
        第二段左端点为 cuts[k]，右端点为 cuts[j]，切割这段木棍的最小成本为 dfs(k,j)。
        成本之和为 dfs(i,k)+dfs(k,j)，再算上切割之前木棍的长度 cuts[j]−cuts[i]，得到
        dfs(i,k) + dfs(k,j) + cuts[j] − cuts[i]
        枚举 k=i+1,i+2,…,j−1，所有成本取最小值，得

        dfs(i,j)= min(k=i+1 ~ j-1){​dfs(i,k)+dfs(k,j)+cuts[j]−cuts[i]}
        其中 cuts[j]−cuts[i] 与 k 无关，可以提到循环外面。

        递归边界：dfs(i,i+1)=0。此时木棍中没有要切割的位置，所以切割成本为 0。
        递归入口：dfs(0,m−1)，也就是答案。其中 m 是添加了 0 和 n 之后的 cuts 数组的长度。"""

        cuts.sort()
        cuts = [0] + cuts + [n]

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> int:
            if i + 1 == j:  # 无需切割
                return 0
            # 枚举切割位置 cuts[k]
            return min(dfs(i, k) + dfs(k, j) for k in range(i + 1, j)) + cuts[j] - cuts[i]

        return dfs(0, len(cuts) - 1)

    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]

        m = len(cuts)
        # dp[i][j]代表从i到j进行切割的最小总成本
        dp = [[0] * m for _ in range(m)]
        for i in range(m - 3, -1, -1):
            for j in range(i + 2, m):
                dp[i][j] = min(dp[i][k] + dp[k][j] for k in range(i + 1, j)) + cuts[j] - cuts[i]
        return dp[0][-1]
