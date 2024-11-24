#
# * 713. 乘积小于 K 的子数组 - M
# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。

# 示例 1：
# 输入：nums = [10,5,2,6], k = 100
# 输出：8
# 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2]、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
# 示例 2：
# 输入：nums = [1,2,3], k = 0
# 输出：0

# 提示:
# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106

from math import log
from bisect import bisect_right


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        """滑动窗口"""
        # 小技巧：特判 k=0 和 k=1，这样 while 循环中就无需判断 left <= right 了。
        if k <= 1:
            return 0
        n = len(nums)
        ans = 0
        prod = 1
        left = 0
        for right, num in enumerate(nums):
            prod *= num
            while left <= right and prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

    def numSubarrayProductLessThanK2(self, nums: list[int], k: int) -> int:
        """二分查找，防止溢出，使用对数，
           枚举子数组的右端点 j，在 logPrefix 的区间 [0,j] 内二分查找满足
           logPrefix[j+1]−logPrefix[l]<logk 即 logPrefix[l]>logPrefix[j+1]−logk 的最小下标 l，
           那么以 j 为右端点且元素乘积小于 k 的子数组数目为 j+1−l。返回所有数目之和。

           double 类型只能保证 15 位有效数字是精确的。为了避免计算带来的误差，我们将不等式 logPrefix[l]>logPrefix[j+1]−logk 的右边加上 10^−10
        （题目中的 double 数值整数部分的数字不超过5个），即 logPrefix[l]>logPrefix[j+1]−logk+10^−10，从而防止不等式两边数值相等却被判定为大于的情况。
        """
        if k == 0:
            return 0
        ans, n = 0, len(nums)
        logPrefix = [0] * (n + 1)
        for i, num in enumerate(nums):
            logPrefix[i + 1] = logPrefix[i] + log(num)
        logK = log(k)
        for j in range(1, n + 1):
            l = bisect_right(logPrefix, logPrefix[j] - logK + 1e-10, 0, j)
            ans += j - l
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    print(sol.numSubarrayProductLessThanK(nums, k))
    print(sol.numSubarrayProductLessThanK2(nums, k))

    nums = [1, 2, 3]
    k = 0
    print(sol.numSubarrayProductLessThanK(nums, k))
    print(sol.numSubarrayProductLessThanK2(nums, k))
