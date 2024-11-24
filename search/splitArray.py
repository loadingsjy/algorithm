#
# * 410. 分割数组的最大值 - H

# 给定一个非负整数数组 nums 和一个整数 k ，你需要将这个数组分成 k 个非空的连续子数组。
# 设计一个算法使得这 k 个子数组各自和的最大值最小。

# 示例 1：
# 输入：nums = [7,2,5,10,8], k = 2
# 输出：18
# 解释：
# 一共有四种方法将 nums 分割为 2 个子数组。
# 其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
# 示例 2：
# 输入：nums = [1,2,3,4,5], k = 2
# 输出：9
# 示例 3：
# 输入：nums = [1,4,4], k = 3
# 输出：4

# 提示：
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 106
# 1 <= k <= min(50, nums.length)


class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        """二分答案法，时间复杂度O(nlogk), k = sum-max"""

        def f(limit):
            """划分每个部分的累加和都小于等于limit，最少划分成几分"""
            part = 1
            sum_ = 0
            for num in nums:
                if sum_ + num > limit:
                    part += 1
                    sum_ = num
                else:
                    sum_ += num
            return part

        ans = 0
        l, r = max(nums), sum(nums)  # 答案可能的范围
        while l <= r:
            mid = (l + r) // 2
            if f(mid) <= k:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
