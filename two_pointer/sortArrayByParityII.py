#
# * 922. 按奇偶排序数组 II - E
# 给定一个非负整数数组 nums，  nums 中一半整数是 奇数 ，一半整数是 偶数 。
# 对数组进行排序，以便当 nums[i] 为奇数时，i 也是 奇数 ；当 nums[i] 为偶数时， i 也是 偶数 。
# 你可以返回 任何满足上述条件的数组作为答案 。

# 示例 1：
# 输入：nums = [4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
# 示例 2：
# 输入：nums = [2,3]
# 输出：[2,3]

# 提示：
# 2 <= nums.length <= 2 * 10^4
# nums.length 是偶数
# nums 中一半是偶数
# 0 <= nums[i] <= 1000

# 进阶：可以不使用额外空间解决问题吗？


class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        """双指针，数组的最后一个数当做目前要处理的数"""
        n = len(nums)
        even, odd = 0, 1
        while even < n and odd < n:
            if nums[-1] & 1 == 0:
                nums[even], nums[-1] = nums[-1], nums[even]
                even += 2
            else:
                nums[odd], nums[-1] = nums[-1], nums[odd]
                odd += 2
        return nums

    def sortArrayByParityII2(self, nums):
        """双指针法：
        为数组的偶数下标部分和奇数下标部分分别维护指针 i,j。
        随后，在每一步中，如果 nums[i] 为奇数，则不断地向前移动 j（每次移动两个单位），直到遇见下一个偶数。
        此时，可以直接将 nums[i] 与 nums[j] 交换。我们不断进行这样的过程，最终能够将所有的整数放在正确的位置上。
        """
        n = len(nums)
        i = 0
        j = 1
        while i < n and j < n:
            # 找到偶数位置上的奇数
            while i < n and nums[i] & 1 == 0:
                i += 2
            # 找到奇数位置上的偶数
            while j < n and nums[j] & 1 == 1:
                j += 2
            # 交换
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 2, 5, 7]
    print(sol.sortArrayByParityII(nums))
    print(sol.sortArrayByParityII2(nums))
