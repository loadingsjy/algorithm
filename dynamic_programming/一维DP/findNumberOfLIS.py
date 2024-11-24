#
# * 673. 最长递增子序列的个数 - M
# 给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。
# 注意 这个数列必须是 严格 递增的。
# 示例 1:
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
# 示例 2:
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。

# 提示:
# 1 <= nums.length <= 2000
# -106 <= nums[i] <= 106

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """序列 DP
        与朴素的 LIS 问题（问长度）相比，本题问的是最长上升子序列的个数。
        我们只需要在朴素 LIS 问题的基础上通过「记录额外信息」来进行求解即可。
        在朴素的 LIS 问题中，我们定义 f[i] 为考虑以 nums[i] 为结尾的最长上升子序列的长度。 最终答案为所有 f[0...(n−1)] 中的最大值。
        
        不失一般性地考虑 f[i] 该如何转移：
        由于每个数都能独自一个成为子序列，因此起始必然有 f[i]=1；
        枚举区间 [0,i) 的所有数 nums[j]，如果满足 nums[j]<nums[i]，说明 nums[i] 可以接在 nums[j] 后面形成上升子序列，此时使用 f[j] 更新 f[i]，即有 f[i]=f[j]+1。
        回到本题，由于我们需要求解的是最长上升子序列的个数，因此需要额外定义 g[i] 为考虑以 nums[i] 结尾的最长上升子序列的个数。
        
        结合 f[i] 的转移过程，不失一般性地考虑 g[i] 该如何转移：
        同理，由于每个数都能独自一个成为子序列，因此起始必然有 g[i]=1；
        枚举区间 [0,i) 的所有数 nums[j]，如果满足 nums[j]<nums[i]，说明 nums[i] 可以接在 nums[j] 后面形成上升子序列，这时候对 f[i] 和 f[j]+1 的大小关系进行分情况讨论：
        满足 f[i]<f[j]+1：说明 f[i] 会被 f[j]+1 直接更新，此时同步直接更新 g[i]=g[j] 即可；
        满足 f[i]=f[j]+1：说明找到了一个新的符合条件的前驱，此时将值继续累加到方案数当中，即有 g[i]+=g[j]。
        
        在转移过程，我们可以同时记录全局最长上升子序列的最大长度 max，最终答案为所有满足 f[i]=max 的 g[i] 的累加值。"""
        
        n = len(nums)
        dp = [1] * n  # dp[i] 必须以i为结尾的最长递增子序列的长度
        max_len = [1] * n  # ans[i] 必须以i为结尾的最长递增子序列的个数
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        max_len[i] = max_len[j]
                        dp[i] = dp[j] + 1
                    elif dp[i] == dp[j] + 1:
                        max_len[i] += max_len[j]

        max_length = max(dp)
        ans = 0
        for i, l in enumerate(dp):
            if l == max_length:
                ans += max_len[i]
        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 5, 4, 7]
    print(sol.findNumberOfLIS(nums))