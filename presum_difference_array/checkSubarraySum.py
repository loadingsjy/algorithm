#
# * 连续的子数组和
# 给你一个整数数组 nums 和一个整数 k ，如果 nums 有一个 好的子数组 返回 true ，否则返回 false：
# 一个 好的子数组 是：
# 长度 至少为 2 ，且
# 子数组元素总和为 k 的倍数。
# 注意：
# 子数组 是数组中 连续 的部分。
# 如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终 视为 k 的一个倍数。
# 示例 1：
# 输入：nums = [23,2,4,6,7], k = 6
# 输出：true
# 解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
# 示例 2：
# 输入：nums = [23,2,6,4,7], k = 6
# 输出：true
# 解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。
# 42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
# 示例 3：
# 输入：nums = [23,2,6,4,7], k = 13
# 输出：false


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """当 prefixSums[q] − prefixSums[p] 为 k 的倍数时，prefixSums[p] 和 prefixSums[q] 除以 k 的余数相同。
        因此只需要计算每个下标对应的前缀和除以 k 的余数即可，使用哈希表存储每个余数第一次出现的下标。"""
        n = len(nums)
        all_sum = sum(nums)
        if n < 2:
            return False
        if k == all_sum or all_sum == 0:
            return True

        # key: pre_sum % k,  value:  pre_sum % k 第一次出现的 index
        mp = dict()
        mp[0] = -1
        pre_sum = 0
        for i, num in enumerate(nums):
            pre_sum = pre_sum + num
            remainder = pre_sum % k
            if remainder in mp:
                if i - mp[remainder] >= 2:
                    return True
            else:
                mp[remainder] = i
        return False


if __name__ == "__main__":
    s = Solution()
    nums = [23, 2, 4, 6, 7]
    k = 6
    print(s.checkSubarraySum(nums, k))
