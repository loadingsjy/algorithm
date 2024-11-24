# 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
# 题目数据保证答案符合 32 位整数范围。

# 示例 1：
# 输入：nums = [1,2,3], target = 4
# 输出：7
# 解释：
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 请注意，顺序不同的序列被视作不同的组合。
# 示例 2：
# 输入：nums = [9], target = 3
# 输出：0
from functools import cache

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:

        @cache
        def dfs(target):
            if target == 0:
                return 1
            ans = 0
            for num in nums:
                if num <= target:
                    p = dfs(target - num)
                    ans += p
            return ans

        return dfs(target)

    def combinationSum4_2(self, nums: list[int], target: int) -> int:
        """动态规划"""
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            dp[i] = sum(dp[i - x] for x in nums if x <= i)
        return dp[target]


