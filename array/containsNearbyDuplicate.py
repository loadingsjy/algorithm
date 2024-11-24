#
# * 219. 存在重复元素 II
# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。
# 如果存在，返回 true ；否则，返回 false 。

# 示例 1：
# 输入：nums = [1,2,3,1], k = 3
# 输出：true
# 示例 2：
# 输入：nums = [1,0,1,1], k = 1
# 输出：true
# 示例 3：
# 输入：nums = [1,2,3,1,2,3], k = 2
# 输出：false


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """哈希表"""
        n = len(nums)
        last_cur = dict()  # key: 数字, value：最近一次出现的index

        for i, num in enumerate(nums):
            if num in last_cur and i - last_cur[num] <= k:
                return True
            last_cur[num] = i
        return False

    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """考虑数组 nums 中的每个长度不超过 k+1 的滑动窗口，同一个滑动窗口中的任意两个下标差的绝对值不超过 k。
        如果存在一个滑动窗口，其中有重复元素，则存在两个不同的下标 i 和 j 满足 nums[i]=nums[j] 且 ∣i−j∣≤k。
        如果所有滑动窗口中都没有重复元素，则不存在符合要求的下标。因此，只要遍历每个滑动窗口，判断滑动窗口中是否有重复元素即可。
        """
        s = set()
        for i, num in enumerate(nums):
            if i > k:  # 大小为k + 1的滑动窗口中的任意两个下标差的绝对值不超过k
                s.remove(nums[i - k - 1])
            if num in s:
                return True
            s.add(num)
        return False
