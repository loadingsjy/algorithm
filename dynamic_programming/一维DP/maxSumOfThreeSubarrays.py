#
# * 689. 三个无重叠子数组的最大和 - H
# 给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且全部数字和（3 * k 项）最大的子数组，并返回这三个子数组。
# 以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。

# 示例 1：
# 输入：nums = [1,2,1,2,6,7,5,1], k = 2
# 输出：[0,3,5]
# 解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
# 也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
# 示例 2：
# 输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
# 输出：[0,2,4]

# 提示：
# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] < 216
# 1 <= k <= floor(nums.length / 3)


class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        """预处理前后缀 + 枚举中间子数组"""
        n = len(nums)
        k_sum = [0] * n  # k_sum[i]代表以i位置开头的k的数字之和为多少
        pre_sum = sum(nums[:k])
        k_sum[0] = pre_sum
        for i in range(0, n - k):
            pre_sum -= nums[i]
            pre_sum += nums[i + k]
            k_sum[i + 1] = pre_sum

        pre_dp = [-1] * n  # pre_dp[i] = 0...i 范围上长度为k的最大累加子数组的开始index
        suf_dp = [-1] * n  # suf_dp[i] = i...n 范围上长度为k的最大累加子数组的开始index

        pre_dp[k - 1] = 0
        for r in range(k, n):
            if k_sum[r - k + 1] > k_sum[pre_dp[r - 1]]:
                pre_dp[r] = r - k + 1
            else:
                pre_dp[r] = pre_dp[r - 1]

        suf_dp[n - k] = n - k
        for l in range(n - k - 1, -1, -1):
            if k_sum[l] >= k_sum[suf_dp[l + 1]]:
                suf_dp[l] = l
            else:
                suf_dp[l] = suf_dp[l + 1]

        a, b, c = 0, 0, 0
        ans = 0
        for l in range(k, n - k):  # 枚举中间范围
            r = l + k - 1
            res = k_sum[pre_dp[l - 1]] + k_sum[l] + k_sum[suf_dp[r + 1]]
            if res > ans:
                ans = res
                a = pre_dp[l - 1]
                b = l
                c = suf_dp[r + 1]
        return a, b, c

    def maxSumOfThreeSubarrays2(self, nums: list[int], k: int) -> list[int]:
        """三个滑动窗口
        我们使用三个大小为 k 的滑动窗口。
        设 sum1为第一个滑动窗口的元素和，该滑动窗口从 [0,k−1] 开始；sum2为第二个滑动窗口的元素和，该滑动窗口从 [k,2k−1] 开始；sum3为第三个滑动窗口的元素和，该滑动窗口从 [2k,3k−1] 开始。

        我们同时向右滑动这三个窗口，按照前言二的方法并维护 maxSum12及其对应位置。
        每次滑动时，计算当前 maxSum12与 sum3之和。统计这一过程中的 maxSum12+sum3的最大值及其对应位置。
        对于题目要求的最小字典序，由于我们是从左向右遍历的，并且仅当元素和超过最大元素和时才修改最大元素和，从而保证求出来的下标列表是字典序最小的。
        """
        ans = []
        sum1, maxSum1, maxSum1Idx = 0, 0, 0
        sum2, maxSum12, maxSum12Idx = 0, 0, ()
        sum3, maxTotal = 0, 0
        for i in range(k * 2, len(nums)):
            sum1 += nums[i - k * 2]
            sum2 += nums[i - k]
            sum3 += nums[i]
            if i >= k * 3 - 1:
                if sum1 > maxSum1:
                    maxSum1 = sum1
                    maxSum1Idx = i - k * 3 + 1
                if maxSum1 + sum2 > maxSum12:
                    maxSum12 = maxSum1 + sum2
                    maxSum12Idx = (maxSum1Idx, i - k * 2 + 1)
                if maxSum12 + sum3 > maxTotal:
                    maxTotal = maxSum12 + sum3
                    ans = [*maxSum12Idx, i - k + 1]
                sum1 -= nums[i - k * 3 + 1]
                sum2 -= nums[i - k * 2 + 1]
                sum3 -= nums[i - k + 1]
        return ans
