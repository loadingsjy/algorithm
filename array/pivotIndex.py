#
# * 724. 寻找数组的中心下标
# 给你一个整数数组 nums ，请计算数组的 中心下标 。
# 数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
# 如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
# 如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。

# 示例 1：
# 输入：nums = [1, 7, 3, 6, 5, 6]
# 输出：3
# 解释：
# 中心下标是 3 。
# 左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
# 右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum_ = sum(nums)
        nums = [0] + nums + [0]

        pre_sum = 0
        for i, num in enumerate(nums[1:-1]):
            if pre_sum == sum_ - num - pre_sum:
                return i
            pre_sum += num
        return -1
    
    def pivotIndex2(self, nums: list[int]) -> int:
        s = sum(nums)
        left_s = 0
        for i, x in enumerate(nums):
            if left_s * 2 == s - x:
                return i
            left_s += x
        return -1

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    print(sol.pivotIndex(nums))
