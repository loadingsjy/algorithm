# 2831. 找出最长等值子数组
# 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
# 如果子数组中所有元素都相等，则认为子数组是一个等值子数组 。注意，空数组是等值子数组 。
# 从 nums 中删除最多 k 个元素后，返回可能的最长等值子数组的长度。
# 子数组 是数组中一个连续且可能为空的元素序列。
# 示例 1：
# 输入：nums = [1,3,2,3,1,3], k = 3
# 输出：3
# 解释：最优的方案是删除下标 2 和下标 4 的元素。
# 删除后，nums 等于 [1, 3, 3, 3] 。
# 最长等值子数组从 i = 1 开始到 j = 3 结束，长度等于 3 。
# 可以证明无法创建更长的等值子数组。
# 示例 2：
# 输入：nums = [1,1,2,2,1,1], k = 2
# 输出：4
# 解释：最优的方案是删除下标 2 和下标 3 的元素。
# 删除后，nums 等于 [1, 1, 1, 1] 。
# 数组自身就是等值子数组，长度等于 4 。
# 可以证明无法创建更长的等值子数组。
from collections import defaultdict


class Solution:
    def longestEqualSubarray(self, nums: list[int], k: int) -> int:
        """分组 + 滑动窗口"""
        pos = defaultdict(list)
        # 把相同元素分组，相同元素的下标记录到哈希表
        for i, num in enumerate(nums):
            pos[num].append(i)

        ans = 0
        for vec in pos.values():
            left = 0
            for right in range(len(vec)):
                # 缩小窗口，直到不同元素数量小于等于 k
                while vec[right] - vec[left] - (right - left) > k:
                    left += 1
                ans = max(ans, right - left + 1)

        return ans

    def longestEqualSubarray2(self, nums: list[int], k: int) -> int:
        """改进"""
        pos_lists = defaultdict(list)
        for i, x in enumerate(nums):
            pos_lists[x].append(i - len(pos_lists[x]))

        ans = 0
        for pos in pos_lists.values():
            if len(pos) <= ans:
                continue  # 无法让 ans 变得更大
            left = 0
            for right, p in enumerate(pos):
                while p - pos[left] > k:  # 要删除的数太多了
                    left += 1
                ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 2, 3, 1, 3]
    k = 3
    print(s.longestEqualSubarray(nums, k))
    print(s.longestEqualSubarray2(nums, k))
