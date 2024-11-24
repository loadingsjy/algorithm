#
# * 485. 最大连续 1 的个数
# 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

# 示例 1：
# 输入：nums = [1,1,0,1,1,1]
# 输出：3
# 解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
# 示例 2:
# 输入：nums = [1,0,1,1,0,1]
# 输出：2

# 提示：
# 1 <= nums.length <= 105
# nums[i] 不是 0 就是 1.


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """双指针法"""
        n = len(nums)
        ans = 0
        left, right = 0, -1
        while left < n:
            if nums[left] == 0:
                left += 1
                continue
            right = left
            while right + 1 < n and nums[right + 1] == 1:
                right += 1
            ans = max(ans, right - left + 1)
            left = right + 1
        return ans

    def findMaxConsecutiveOnes2(self, nums: list[int]) -> int:
        """为了得到数组中最大连续 1 的个数，需要遍历数组，并记录最大的连续 1 的个数和当前的连续 1 的个数。
        如果当前元素是 1，则将当前的连续 1 的个数加 1，否则，使用之前的连续 1 的个数更新最大的连续 1 的个数，并将当前的连续 1 的个数清零。

        遍历数组结束之后，需要再次使用当前的连续 1 的个数更新最大的连续 1 的个数，因为数组的最后一个元素可能是 1，
        且最长连续 1 的子数组可能出现在数组的末尾，如果遍历数组结束之后不更新最大的连续 1 的个数，则会导致结果错误。
        """
        ans = 0
        length = 0
        for num in nums:
            if num == 1:
                length += 1
            else:
                ans = max(ans, length)
                length = 0
        ans = max(ans, length)
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 0, 1, 1, 1]
    print(s.findMaxConsecutiveOnes(nums))
    print(s.findMaxConsecutiveOnes2(nums))

    nums = [1, 0, 1, 1, 0, 1]
    print(s.findMaxConsecutiveOnes(nums))
    print(s.findMaxConsecutiveOnes2(nums))
