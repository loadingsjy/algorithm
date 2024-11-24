#
# * 992. K 个不同整数的子数组 - H

# 给定一个正整数数组 nums和一个整数 k，返回 nums 中 「好子数组」 的数目。
# 如果 nums 的某个子数组中不同整数的个数恰好为 k，则称 nums 的这个连续、不一定不同的子数组为 「好子数组 」。
# 例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。
# 子数组 是数组的 连续 部分。

# 示例 1：
# 输入：nums = [1,2,1,2,3], k = 2
# 输出：7
# 解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
# 示例 2：
# 输入：nums = [1,2,1,3,4], k = 3
# 输出：3
# 解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].

# 提示：
# 1 <= nums.length <= 2 * 104
# 1 <= nums[i], k <= nums.length

from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        """超时"""
        n = len(nums)
        cnt = defaultdict(int)
        occ = set()
        ans = 0
        for left, num in enumerate(nums):
            cnt = defaultdict(int)
            occ = set()
            right = left - 1
            while right + 1 < n and (len(occ) < k or nums[right + 1] in occ):
                cnt[nums[right + 1]] += 1
                occ.add(nums[right + 1])
                if len(occ) == k:
                    ans += 1
                right += 1
        return ans

    def subarraysWithKDistinct2(self, nums: list[int], k: int) -> int:
        """把「恰好」改成「最多」就可以使用双指针一前一后交替向右的方法完成，这是因为对于每一个确定的左边界，
        最多包含 K 种不同整数的右边界是唯一确定的，并且在左边界向右移动的过程中，右边界或者在原来的地方，或者在原来地方的右边。
        而「最多存在 K 个不同整数的子区间的个数」与「恰好存在 K 个不同整数的子区间的个数」的差恰好等于「最多存在 K−1 个不同整数的子区间的个数」。

        数组中的不同整数的个数 <= k 的子数组的数量 - 数组中的不同整数的个数 <= k - 1 的子数组的数量 = 数组中不同整数的个数恰好为k的子数组数量
        """

        def numOfMostKinds(nums, k):
            """数组中的不同整数的个数<=k的子数组的数量"""
            n = len(nums)
            cnt = defaultdict(int)
            collected = 0
            ans = 0
            left = 0
            # 窗口[left, right]
            for right, num in enumerate(nums):
                cnt[num] += 1
                if cnt[num] == 1:
                    collected += 1
                while left <= right and collected > k:
                    cnt[nums[left]] -= 1
                    if cnt[nums[left]] == 0:
                        collected -= 1
                    left += 1
                ans += right - left + 1

            return ans

        return numOfMostKinds(nums, k) - numOfMostKinds(nums, k - 1)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 1, 2, 3]
    k = 2
    print(sol.subarraysWithKDistinct(nums, k))
    print(sol.subarraysWithKDistinct2(nums, k))
