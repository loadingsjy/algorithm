#
# * 974. 和可被K整除的子数组 - M

# 给定一个整数数组 nums 和一个整数 k ，返回其中元素之和可被 k 整除的非空 子数组 的数目。
# 子数组 是数组中 连续 的部分。

# 示例 1：
# 输入：nums = [4,5,0,-2,-3,1], k = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 k = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# 示例 2:
# 输入: nums = [5], k = 9
# 输出: 0

from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:

        mp = defaultdict(int)  # key:前缀和 mod k 的结果，value: 出现次数
        mp[0] = 1
        pre_mod = 0
        ans = 0

        for num in nums:
            pre_mod = (pre_mod + num) % k
            if pre_mod in mp:
                ans += mp[pre_mod]
            mp[pre_mod] += 1

        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 0, -2, -3, 1]
    k = 5
    print(s.subarraysDivByK(nums, k))
