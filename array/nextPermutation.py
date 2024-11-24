#
# * 31. 下一个排列
# 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
# 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
# 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
# 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
# 给你一个整数数组 nums ，找出 nums 的下一个排列。
# 必须 原地 修改，只允许使用额外常数空间。

# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[1,3,2]
# 示例 2：
# 输入：nums = [3,2,1]
# 输出：[1,2,3]
# 示例 3：
# 输入：nums = [1,1,5]
# 输出：[1,5,1]
from copy import deepcopy


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        firstIndex = -1
        n = len(nums)

        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                firstIndex = i
                break
        # print(firstIndex)
        if firstIndex == -1:
            reverse(nums, 0, n - 1)
            return
        secondIndex = -1
        for i in range(n - 1, firstIndex, -1):
            if nums[i] > nums[firstIndex]:
                secondIndex = i
                break
        nums[firstIndex], nums[secondIndex] = nums[secondIndex], nums[firstIndex]
        reverse(nums, firstIndex + 1, n - 1)

    def nextPermutation2(self, nums: list[int]) -> None:
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i != 0:
            j = len(nums) - 1
            while nums[j] <= nums[i - 1]:
                j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # 反转 i 后面的部分
        nums[i:] = list(reversed(nums[i:]))


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    n1 = deepcopy(nums)
    n2 = deepcopy(nums)
    s.nextPermutation(n1)
    print(n1)
    s.nextPermutation(n2)
    print(n2)

    print()

    nums = [2, 5, 4, 3, 1]
    n1 = deepcopy(nums)
    n2 = deepcopy(nums)
    s.nextPermutation(n1)
    print(n1)
    s.nextPermutation(n2)
    print(n2)
