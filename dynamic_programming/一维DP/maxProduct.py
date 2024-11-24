# 152. 乘积最大子数组 - M
# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组
# （该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 测试用例的答案是一个 32-位 整数。

# 示例 1:
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

# 提示:
# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# nums 的任何子数组的乘积都 保证 是一个 32-位 整数


from math import inf


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """由于存在负数，那么会导致最大的变最小的，最小的变最大的。因此还需要维护当前最小值imin"""

        n = len(nums)
        if n == 1:
            return nums[0]
        dp_max = [-inf] * n  # dp_max[i]表示必须以nums[i]为结尾的最大子数组乘积
        dp_min = [inf] * n  # dp_min[i]表示必须以nums[i]为结尾的最小子数组乘积
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i, num in enumerate(nums[1:]):
            if num >= 0:
                dp_max[i + 1] = max(dp_max[i] * num, num)
                dp_min[i + 1] = min(dp_min[i] * num, num)
            else:
                dp_max[i + 1] = max(dp_min[i] * num, num)
                dp_min[i + 1] = min(dp_max[i] * num, num)
        return max(dp_max)

    def maxProduct2(self, nums: list[int]) -> int:
        """由于存在负数，那么会导致最大的变最小的，最小的变最大的。因此还需要维护当前最小值imin"""
        if not nums:
            return
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, -2, 4]
    print(sol.maxProduct(nums))
    print(sol.maxProduct2(nums))
