# 719. 找出第 K 小的数对距离

# 数对 (a,b) 由整数 a 和 b 组成，其数对距离定义为 a 和 b 的绝对差值。
# 给你一个整数数组 nums 和一个整数 k ，数对由 nums[i] 和 nums[j] 组成且满足 0 <= i < j < nums.length 。返回 所有数对距离中 第 k 小的数对距离。

# 示例 1：
# 输入：nums = [1,3,1], k = 1
# 输出：0
# 解释：数对和对应的距离如下：
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# 距离第 1 小的数对是 (1,1) ，距离为 0 。
# 示例 2：
# 输入：nums = [1,1,1], k = 2
# 输出：0
# 示例 3：
# 输：nums = [1,6,1], k = 3
# 输出：5

# 提示：
# n == nums.length
# 2 <= n <= 10^4
# 0 <= nums[i] <= 10^6
# 1 <= k <= n * (n - 1) / 2
from bisect import bisect_left


class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        """时间复杂度O(nlogn) + nlog(max-min)， 空间复杂度O(1)"""
        n = len(nums)
        nums.sort()

        def count(limit):
            """返回数组中两数差值小于k的数对数量"""
            ans = 0
            right = -1
            # 滑动窗口法，必须是排序好的数组
            for left, num in enumerate(nums):
                while right + 1 < n and nums[right + 1] - num <= limit:
                    right += 1
                ans += right - left
            return ans

        # 二分答案法
        l, r = 0, max(nums) - min(nums)
        while l <= r:
            mid = (l + r) // 2
            if count(mid) >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l

    def smallestDistancePair2(self, nums: list[int], k: int) -> int:
        """排序 + 二分查找"""

        def count(mid: int) -> int:
            cnt = 0
            for j, num in enumerate(nums):
                i = bisect_left(nums, num - mid, 0, j)
                cnt += j - i
            return cnt

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), k, key=count)

    def smallestDistancePair3(self, nums: list[int], k: int) -> int:
        """排序 + 二分查找 + 双指针"""

        def count(mid: int) -> int:
            cnt = i = 0
            for j, num in enumerate(nums):
                while num - nums[i] > mid:
                    i += 1
                cnt += j - i
            return cnt

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), k, key=count)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 6, 1]
    k = 3
    print(sol.smallestDistancePair(nums, k))
    print(sol.smallestDistancePair2(nums, k))
    print(sol.smallestDistancePair3(nums, k))
