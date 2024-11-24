# * 和为k的子数组
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
# 子数组是数组中元素的连续非空序列。
# 示例 1：
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：
# 输入：nums = [1,2,3], k = 3
# 输出：2
from collections import defaultdict


class Solution:
    def subarraySum_my(self, nums: list[int], k: int) -> int:
        """超时"""
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if pre_sum[j + 1] - pre_sum[i] == k:
                    ans += 1
        return ans

    def subarraySum(self, nums: list[int], k: int) -> int:
        """前缀和 + 哈希表优化"""
        """我们考虑以 i 结尾的和为 k 的连续子数组个数时只要统计有多少个前缀和为 pre[i]−k 的 pre[j] 即可。
        我们建立哈希表 mp，以和为键，出现次数为对应的值，记录 pre[i] 出现的次数，
        从左往右边更新 mp 边计算答案，那么以 i 结尾的答案 mp[pre[i]−k] 即可在 O(1) 时间内得到。最后的答案即为所有下标结尾的和为 k 的子数组个数之和。
        
        需要注意的是，从左往右边更新边计算的时候已经保证了mp[pre[i]−k] 里记录的 pre[j] 的下标范围是 0≤j≤i 。
        同时，由于pre[i] 的计算只与前一项的答案有关，因此我们可以不用建立 pre 数组，直接用 pre 变量来记录 pre[i−1] 的答案即可。"""

        n = len(nums)
        count = 0
        pre_sum = 0
        # key:前缀和, value:计数
        mp = defaultdict(int)
        # 0这个前缀和，再没有任何数字的时候，就已经有了1次
        mp[0] = 1
        for i in range(n):
            pre_sum += nums[i]
            # 求以i为结尾的和为k的子数组的个数(pre[i] - (pre[i] - k) == k)
            count += mp[pre_sum - k]
            mp[pre_sum] += 1

        return count


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1]
    k = 2
    print(s.subarraySum_my(nums, k))
    print(s.subarraySum(nums, k))
