# 最大整数拆分
# 给定一个正整数 n，将其拆分为至少两个正整数的和，使得它们的乘积最大。

# 示例 1:
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。

# 示例 2:
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。

# 解题思路：
# 这道题的思路是动态规划。
# 我们可以定义 dp[i] 表示将 i 拆分为至少两个正整数的和的最大乘积。
# 状态转移方程如下：
# dp[i] = max(dp[j] * dp[i-j]) (1 ≤ j ≤ i/2)
# 解释：
# 假设 i 拆分为 j 和 i-j，那么 j 乘以 i-j 就是 i。
# 所以，我们可以枚举 j，然后计算 dp[j] * dp[i-j] 作为候选值，取其最大值。
# 最后，我们返回 dp[n] 作为答案。
# 时间复杂度：O(n^2)
# 空间复杂度：O(n)


class Solution:
    def maxProduct(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i//2+1):
                dp[i] = max(dp[i], dp[j] * dp[i-j])
        return dp[n]
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct(2))
    print(s.maxProduct(10))