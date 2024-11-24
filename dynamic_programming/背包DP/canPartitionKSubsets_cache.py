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

        nums.sort()
        n = len(nums)

        @cache
        def dfs(s, p):
            '''函数 表示当前桶目前有这么多数字可用，并且已经放了总量为p(模div)的物品了, 接下来能不能正好放满？
            s表示目前可用数字集合，s第i位为1表示nums[i]数字可用，s第i位为0表示nums[i]数字已经用过了'''
            if s == 0:
                return True
            for i in range(n):
                if nums[i] + p > div:
                    break
                # 没有超过容量，并且nums[i]数字可用，并且已经放了总量为p的物品了，继续放会不会正好满
                # s >> i & 1 的前提下 s ^ (1 << i) 表示将s的第i为置零，表示放入数字
                if s >> i & 1 and dfs(s ^ (1 << i), (p + nums[i]) % div):  # p + nums[i] 等于 per 时置为 0 (表示当前桶已经正好满了)
                    return True
            return False
    
        return dfs((1 << n) - 1, 0)
    
    # 根据上面暴力递归，改成动态规化
    
    def canPartitionKSubsets_dp(self, nums, k):
        if not nums or len(nums) < k:
            return False

        _sum = sum(nums)
        div, mod = divmod(_sum, k)

        if mod or max(nums) > div:
            return False

        nums.sort()
        n = len(nums)
        dp = [False] * (1 << n)
        dp[0] = True
        cursum = [0] * (1 << n)
        for i in range(0, 1 << n):
            if not dp[i]:
                continue
            for j in range(n):
                if cursum[i] + nums[j] > div:
                    break
                if (i >> j & 1) == 0:       # 如果取第j个数字，数组正好取空了
                    next = i | (1 << j)
                    if not dp[next]:
                        cursum[next] = (cursum[i] + nums[j]) % div
                        dp[next] = True
        # print(dp)
        return dp[(1 << n) - 1]
    


if __name__ == "__main__":
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    s = Solution()
    print(s.canPartitionKSubsets(nums, k))
    print(s.canPartitionKSubsets_dp(nums,k))
    nums = [
        3522,
        181,
        521,
        515,
        304,
        123,
        2512,
        312,
        922,
        407,
        146,
        1932,
        4037,
        2646,
        3871,
        269,
    ]
    k = 5
    print(s.canPartitionKSubsets(nums, k))
    print(s.canPartitionKSubsets_dp(nums,k))
