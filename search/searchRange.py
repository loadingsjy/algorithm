# 34. 在排序数组中查找元素的第一个和最后一个位置
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
# 示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例 2：
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 示例 3：
# 输入：nums = [], target = 0
# 输出：[-1,-1]

from bisect import bisect_left


class Solution:
    def searchRange_my(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        n = len(nums)
        bound = bisect_left(nums, target)
        if bound == n or nums[bound] != target:
            return [-1, -1]
        right = bound
        while right < n and nums[right] == target:
            right += 1
        return [bound, right - 1]

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        ans = [-1, -1]

        def findFrist(nums, target):
            n = len(nums)

            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low if 0 <= low < n and nums[low] == target else -1

        def findLast(nums, target):
            n = len(nums)
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low - 1 if 0 <= low - 1 < n and nums[low - 1] == target else -1

        ans[0] = findFrist(nums, target)

        if ans[0] == -1:
            return [-1, -1]

        ans[1] = findLast(nums, target)

        return ans

        # right = ans[0]
        # while right < n and nums[right] == target:
        #     right += 1
        # return [ans[0], right - 1]


if __name__ == "__main__":
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(s.searchRange(nums, target))
