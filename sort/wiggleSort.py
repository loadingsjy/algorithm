#
# * 280. 摆动排序 - M

# 给你一个的整数数组 nums, 将该数组重新排序后使 nums[0] <= nums[1] >= nums[2] <= nums[3]... 输入数组总是有一个有效的答案。

# 示例 1:
# 输入：nums = [3,5,2,1,6,4]
# 输出：[3,5,1,6,2,4]
# 解释：[1,6,2,5,3,4]也是有效的答案
# 示例 2:
# 输入：nums = [6,6,5,6,3,8]
# 输出：[6,6,5,6,3,8]

# 提示：
# 1 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 104
# 输入的 nums 保证至少有一个答案。

# 进阶：你能在 O(n) 时间复杂度下解决这个问题吗？


class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        奇数位置与偶数位置进行交换
        """
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

    def wiggleSort2(self, nums: list[int]) -> None:
        """贪心:
        1.从 0 开始，到 nums.length - 2，迭代遍历 nums 中的每个元素，因为最后一个元素没有下一个可以交换的元素。
        2.检查是否 i 是偶数且 nums[i] > nums[i + 1]。 如果是，交换 nums[i] 和 nums[i + 1]。
        3.检查是否 i 是奇数且 nums[i] < nums[i + 1]。 如果是，交换 nums[i] 和 nums[i + 1]。
        """
        for i in range(len(nums) - 1):
            if (i % 2 == 0 and nums[i] > nums[i + 1]) or (
                i % 2 == 1 and nums[i] < nums[i + 1]
            ):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
