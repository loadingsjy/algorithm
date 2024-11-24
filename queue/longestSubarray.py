#
# * 1438. 绝对差不超过限制的最长连续子数组 - H
# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
# 如果不存在满足条件的子数组，则返回 0 。

# 示例 1：
# 输入：nums = [8,2,4,7], limit = 4
# 输出：2
# 解释：所有子数组如下：
# [8] 最大绝对差 |8-8| = 0 <= 4.
# [8,2] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
# [2] 最大绝对差 |2-2| = 0 <= 4.
# [2,4] 最大绝对差 |2-4| = 2 <= 4.
# [2,4,7] 最大绝对差 |2-7| = 5 > 4.
# [4] 最大绝对差 |4-4| = 0 <= 4.
# [4,7] 最大绝对差 |4-7| = 3 <= 4.
# [7] 最大绝对差 |7-7| = 0 <= 4.
# 因此，满足题意的最长子数组的长度为 2 。
# 示例 2：
# 输入：nums = [10,1,2,4,7,2], limit = 5
# 输出：4
# 解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
from sortedcontainers import SortedList
from collections import deque


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        """滑动窗口 + 有序表"""
        s = SortedList()
        n = len(nums)
        left = right = ret = 0

        while right < n:
            s.add(nums[right])
            while s[-1] - s[0] > limit:
                s.remove(nums[left])
                left += 1
            ret = max(ret, right - left + 1)
            right += 1

        return ret

    def longestSubarray2(self, nums: list[int], limit: int) -> int:
        """滑动窗口 + 单调队列：
        两个单调队列，一个单调队列增维护窗口内的最小值，另一个单调队列维护窗口内的最大值"""
        queMax, queMin = deque(), deque()
        left = right = ans = 0

        for right, num in enumerate(nums):
            while queMax and nums[queMax[-1]] <= num:
                queMax.pop()
            while queMin and nums[queMin[-1]] >= num:
                queMin.pop()

            queMax.append(right)
            queMin.append(right)

            while queMax and queMin and nums[queMax[0]] - nums[queMin[0]] > limit:
                if left == queMin[0]:
                    queMin.popleft()
                if left == queMax[0]:
                    queMax.popleft()
                left += 1
            ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [10, 1, 2, 4, 7, 2]
    limit = 5
    print(s.longestSubarray(nums, limit))
    print(s.longestSubarray2(nums, limit))
