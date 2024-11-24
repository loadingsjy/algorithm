#
# * 41. 缺失的第一个正数 - H
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

# 示例 1：
# 输入：nums = [1,2,0]
# 输出：3
# 解释：范围 [1,2] 中的数字都在数组中。
# 示例 2：
# 输入：nums = [3,4,-1,1]
# 输出：2
# 解释：1 在数组中，但 2 没有。
# 示例 3：
# 输入：nums = [7,8,9,11,12]
# 输出：1
# 解释：最小的正数 1 没有出现。

# 提示：
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        """循环不变量：
        1.left: 下标 [0 : left-1] 上的数是我们需要的数，即0 ~ left-1每个位置都满足nums[i] == i+1
        2.right（两个含义）:
        1)下标[right : 最后] 表示垃圾区，这些是无用数字;
        2)目前最好情况下1~right的数都能收集全
        """
        l, r = 0, len(nums)
        while l < r:
            if nums[l] == l + 1:
                l += 1
            elif nums[l] <= l or nums[l] > r or nums[nums[l] - 1] == nums[l]:
                r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            else:
                nums[l], nums[r - 1] = nums[r - 1], nums[l]
        return l + 1


if __name__ == "__main__":
    sol = Solution()
    nums = [-3, 2, 1, 8, 5, 4, 2, 3, 5, 13]
