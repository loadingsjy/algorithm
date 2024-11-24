#
# * 2824. 统计和小于目标的下标对数目
# 给你一个下标从 0 开始长度为 n 的整数数组 nums 和一个整数 target ，请你返回满足 0 <= i < j < n 且 nums[i] + nums[j] < target 的下标对 (i, j) 的数目。
# 示例 1：
# 输入：nums = [-1,1,2,3,1], target = 2
# 输出：3
# 解释：总共有 3 个下标对满足题目描述：
# - (0, 1) ，0 < 1 且 nums[0] + nums[1] = 0 < target
# - (0, 2) ，0 < 2 且 nums[0] + nums[2] = 1 < target
# - (0, 4) ，0 < 4 且 nums[0] + nums[4] = 0 < target
# 注意 (0, 3) 不计入答案因为 nums[0] + nums[3] 不是严格小于 target 。

from itertools import combinations
from bisect import bisect_left


class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        """双指针法"""
        if len(nums) < 2:
            return 0
        nums.sort()
        ans = 0
        n = len(nums)
        left = 0
        right = n - 1
        # 最小的两个数相加都大于或等于target，那么所有的组合都不满足，答案为0个
        if nums[0] + nums[1] >= target:
            return 0
        # 最大的两个数相加都小于target，那么全部的组合都是答案
        if nums[n - 1] + nums[n - 2] < target:
            return n * (n - 1) // 2

        while left < right:
            if nums[left] + nums[right] >= target:
                right -= 1
            elif nums[left] + nums[right] < target:
                ans += right - left
                left += 1
        return ans

    def countPairs2(self, nums: list[int], target: int) -> int:
        """暴力枚举"""
        return sum(x + y < target for x, y in combinations(nums, 2))

    def countPairs3(self, nums: list[int], target: int) -> int:
        """二分查找"""
        nums.sort()
        return sum(
            bisect_left(nums, target - nums[i], 0, i) for i in range(1, len(nums))
        )


if __name__ == "__main__":
    s = Solution()
    nums = [-1, 1, 2, 3, 1]
    target = 2
    print(s.countPairs(nums, target))
    print(s.countPairs2(nums, target))
    print(s.countPairs3(nums, target))

    nums = [-6, 2, 5, -2, -7, -1, 3]
    target = -2
    print(s.countPairs(nums, target))
    print(s.countPairs2(nums, target))
    print(s.countPairs3(nums, target))
