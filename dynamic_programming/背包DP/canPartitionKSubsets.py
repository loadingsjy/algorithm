# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
# 示例 1：
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
# 示例 2:
# 输入: nums = [1,2,3,4], k = 3
# 输出: false

# 提示：
# 1 <= k <= len(nums) <= 16
# 0 < nums[i] < 10000
# 每个元素的频率在 [1,4] 范围内
from functools import cache

class Solution:
    # 回溯法
    def canPartitionKSubsets(self, nums, k):
        if not nums or len(nums) < k:
            return False

        _sum = sum(nums)
        div, mod = divmod(_sum, k)

        if mod or max(nums) > div:
            return False

        nums.sort(reverse=True)     # 从大到小排序，先放大的数
        target = [div] * k

        return self.dfs(nums, k, 0, target)


    def dfs(self, nums, k, index, target):
        if index == len(nums):
            return True
        
        num = nums[index]
        for i in range(k):
            # 剪枝：要么正好放，要么放完以后，至少能放一个最小的
            if target[i] == num  or (index < len(nums) and target[i] - num >= nums[-1]):
                target[i] -= num
                if self.dfs(nums, k, index + 1, target):
                    return True
                target[i] += num
        return False

    # 动态规划
    def canPartitionKSubsets_dp(self, nums, k):
        all = sum(nums)
        if all % k:
            return False
        per = all // k
        nums.sort()
        if nums[-1] > per:
            return False

        n = len(nums)
        dp = [False] * (1 << n)
        dp[0] = True
        cursum = [0] * (1 << n)
        for i in range(0, 1 << n):
            if not dp[i]:
                continue
            for j in range(n):
                if cursum[i] + nums[j] > per:
                    break
                if (i >> j & 1) == 0:       # 如果取第j个数字，数组正好取空了
                    next = i | (1 << j)
                    if not dp[next]:
                        cursum[next] = (cursum[i] + nums[j]) % per
                        dp[next] = True
        # print(dp)
        return dp[(1 << n) - 1]


if __name__ == "__main__":
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    s = Solution()
    print(s.canPartitionKSubsets(nums, k))
    print(s.canPartitionKSubsets_dp(nums, k))
    print()
    
    nums = [3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269]
    k = 5
    print(s.canPartitionKSubsets(nums, k))
    print(s.canPartitionKSubsets_dp(nums, k))
