# 有 A 和 B 两种类型 的汤。一开始每种类型的汤有 n 毫升。有四种分配操作：
# 提供 100ml 的 汤A 和 0ml 的 汤B 。
# 提供 75ml 的 汤A 和 25ml 的 汤B 。
# 提供 50ml 的 汤A 和 50ml 的 汤B 。
# 提供 25ml 的 汤A 和 75ml 的 汤B 。
# 当我们把汤分配给某人之后，汤就没有了。每个回合，我们将从四种概率同为 0.25 的操作中进行分配选择。如果汤的剩余量不足以完成某次操作，我们将尽可能分配。当两种类型的汤都分配完时，停止操作。
# 注意 不存在先分配 100 ml 汤B 的操作。
# 需要返回的值： 汤A 先分配完的概率 +  汤A和汤B 同时分配完的概率 / 2。返回值在正确答案 10-5 的范围内将被认为是正确的。

# 示例 1:
# 输入: n = 50
# 输出: 0.62500
# 解释:如果我们选择前两个操作，A 首先将变为空。
# 对于第三个操作，A 和 B 会同时变为空。
# 对于第四个操作，B 首先将变为空。
# 所以 A 变为空的总概率加上 A 和 B 同时变为空的概率的一半是 0.25 *(1 + 1 + 0.5 + 0)= 0.625。
# 示例 2:
# 输入: n = 100
# 输出: 0.71875
import math


class Solution:
    def soupServings(self, n: int) -> float:
        return self.f(n, n)

    def soupServings_memory(self, n: int) -> float:
        n = math.ceil(n / 25)
        dp = [[-1.0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0.5
        for i in range(1, n + 1):
            dp[0][i] = 1.0
            dp[i][0] = 0.0

        return self.f_memory(n, n, dp)

    def f(self, restA, restB):
        if restA == 0 and restB == 0:
            return 0.5
        elif restA == 0 and restB > 0:
            return 1.0
        elif restA > 0 and restB == 0:
            return 0.0
        else:
            p = 0
            p += self.f(max(restA - 100, 0), restB) * 0.25
            p += self.f(max(restA - 75, 0), max(restB - 25, 0)) * 0.25
            p += self.f(max(restA - 50, 0), max(restB - 50, 0)) * 0.25
            p += self.f(max(restA - 25, 0), max(restB - 75, 0)) * 0.25
        return p

    def f_memory(self, restA, restB, dp):
        if restA == 0 and restB == 0:
            return dp[0][0]
        elif restA == 0 and restB > 0:
            return dp[0][restB]
        elif restA > 0 and restB == 0:
            return dp[restA][0]
        else:
            p = 0
            a1, a2 = max(restA - 4, 0), restB
            b1, b2 = max(restA - 3, 0), max(restB - 1, 0)
            c1, c2 = max(restA - 2, 0), max(restB - 2, 0)
            d1, d2 = max(restA - 1, 0), max(restB - 3, 0)

            if dp[a1][a2] != -1.0:
                p += dp[a1][a2] * 0.25
            else:
                p += self.f_memory(a1, a2, dp) * 0.25

            if dp[b1][b2] != -1.0:
                p += dp[b1][b2] * 0.25
            else:
                p += self.f_memory(b1, b2, dp) * 0.25

            if dp[c1][c2] != -1.0:
                p += dp[c1][c2] * 0.25
            else:
                p += self.f_memory(c1, c2, dp) * 0.25

            if dp[d1][d2] != -1.0:
                p += dp[d1][d2] * 0.25
            else:
                p += self.f_memory(d1, d2, dp) * 0.25

            dp[restA][restB] = p

        return dp[restA][restB]

    def soupServings_dp(self, n):
        '''
        我们可以发现，每次分配操作有 (4,0),(3,1),(2,2),(1,3) 四种，那么在一次分配中，汤 A 平均会被分配的份数期望为 E(A)=(4+3+2+1)×0.25=2.5 ，
        汤 B 平均会被分配的份数期望为 E(B)=(0+1+2+3)×0.25=1.5。
        因此在 n 非常大的时候，汤 A 会有很大的概率比 B 先分配完，汤 A 被先取完的概率应该非常接近 1。
        事实上，当我们进行实际计算时发现，当 n≥4475 时，所求概率已经大于 0.99999 了（可以通过上面的动态规划方法求出），
        它和 1 的误差（无论是绝对误差还是相对误差）都小于 10 −5。实际我们在进行测算时发现：
        n=4475,p≈0.999990211307
        n=4476,p≈0.999990468596
        因此在 n≥179×25 时，我们只需要输出 1 作为答案即可。在其它的情况下，我们使用动态规划计算出答案。
        '''
        n = math.ceil(n / 25)
        
        if n >= 179:
            return 1.0
        
        dp = [[0.0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0.5
        for i in range(1, n + 1):
            dp[0][i] = 1.0
            # dp[i][0] = 0.0

        for row in range(1, n + 1):
            for col in range(1, n + 1):
                a1, a2 = max(row - 4, 0), col
                b1, b2 = max(row - 3, 0), max(col - 1, 0)
                c1, c2 = max(row - 2, 0), max(col - 2, 0)
                d1, d2 = max(row - 1, 0), max(col - 3, 0)
                dp[row][col] += dp[a1][a2] * 0.25 + dp[b1][b2] * 0.25 + dp[c1][c2] * 0.25 + \
                        dp[d1][d2] * 0.25
        
        return dp[n][n]
                


if __name__ == "__main__":
    s = Solution()
    n = 380
    # print(s.soupServings(n))
    print(s.soupServings_memory(n))
    print(s.soupServings_dp(n))
    
    n = 999
    print(s.soupServings_dp(n))
    
    n = 4200
    print(s.soupServings_dp(n))

    
    
