#
# * 300. 最长递增子序列 - M
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
# 示例 1：
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 示例 3：
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
# 提示：
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
# 进阶：
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?

import bisect
from functools import cache


def lengthOfLIS(nums: list[int]) -> int:
    """记忆化搜索"""

    @cache
    def dfs(i):
        if i == len(nums) - 1:
            return 1
        max_len = 1
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                max_len = max(max_len, dfs(j) + 1)

        return max_len

    return max(dfs(i) for i in range(len(nums)))


# 最长递增子序列的长度(不一定是连续的)（动态规划）
def lengthOfLIS2(nums):
    """动态规划： 时间复杂度O(n^2)"""
    n = len(nums)
    dp = [1] * n  # dp[i] 必须以i为结尾的最长递增子序列的长度
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # 不一定是以最后一个元素为结尾的子序列是最长的，所以要遍历所有元素取最大的
    return max(dp)


def lengthOfLIS_greedy(nums):
    """贪心算法： 每次都保证选的递增子序列的末尾元素是最小的，那么选到最后递增子序列的长一定是最长的
    时间复杂度O(nlogn)"""

    """bisect.bisect和bisect.bisect_right返回大于x的第一个下标(相当于C++中的upper_bound)，
    bisect.bisect_left返回大于等于x的第一个下标(相当于C++中的lower_bound)。"""

    # ends[i] 表示长度为i+1的递增子序列中的末尾元素的最小值，ends数组一定严格递增，所以可以二分查找
    ends = []
    ans = 0
    for x in nums:
        j = bisect.bisect_left(ends, x)
        if j == len(ends):
            ends.append(x)
            ans += 1
        else:
            ends[j] = x
    return ans


# Longest Continuous Increasing Subarray
# 最长连续递增子数组的长度（必须是连续的）（动态规划）
def length_of_LCIS(nums):
    n = len(nums)
    dp = [1] * n  # dp[i] stores the length of LCIS ending at i
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            dp[i] = dp[i - 1] + 1
    return max(dp)


if __name__ == "__main__":
    nums = [1, 10, 9, 2, 5, 3, 7, 31, 18, 20]
    # print("nums: ", nums)
    print("lengthOfLIS:  ", lengthOfLIS(nums))
    print("lengthOfLIS:  ", lengthOfLIS2(nums))
    print("lengthOfLIS:  ", lengthOfLIS_greedy(nums))

    print("lengthOfLCIS: ", length_of_LCIS(nums))
