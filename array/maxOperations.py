#
# 1679. K 和数对的最大数目 - M
# 给你一个整数数组 nums 和一个整数 k 。
# 每一步操作中，你需要从数组中选出和为 k 的两个整数，并将它们移出数组。
# 返回你可以对数组执行的最大操作数。

# 示例 1：
# 输入：nums = [1,2,3,4], k = 5
# 输出：2
# 解释：开始时 nums = [1,2,3,4]：
# - 移出 1 和 4 ，之后 nums = [2,3]
# - 移出 2 和 3 ，之后 nums = []
# 不再有和为 5 的数对，因此最多执行 2 次操作。
# 示例 2：
# 输入：nums = [3,1,3,4,3], k = 6
# 输出：1
# 解释：开始时 nums = [3,1,3,4,3]：
# - 移出前两个 3 ，之后nums = [1,4,3]
# 不再有和为 6 的数对，因此最多执行 1 次操作。

# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= k <= 10^9

from collections import Counter


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        """双指针算法"""
        nums.sort()
        n = len(nums)
        if n > 1 and nums[0] + nums[1] > k:
            return 0
        if n > 1 and nums[-1] + nums[-2] < k:
            return 0
        ans = 0
        i, j = 0, n - 1
        while i < j:
            t = nums[i] + nums[j]
            if t == k:
                ans += 1
                i += 1
                j -= 1
            elif t < k:
                i += 1
            else:
                j -= 1
        return ans

    def maxOperations(self, nums: list[int], k: int) -> int:
        """哈希表
        每次先看看哈希表中是否有 k−nums[i]，有就去掉哈希表中的一个 k−nums[i]，同时把答案加一，没有就把 nums[i] 加入哈希表"""
        ans = 0
        cnt = Counter()
        for x in nums:
            if cnt[k - x]:
                cnt[k - x] -= 1
                ans += 1
            else:
                cnt[x] += 1
        return ans
