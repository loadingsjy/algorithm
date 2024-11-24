#
# * 169. 多数元素
# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

# 示例 1：
# 输入：nums = [3,2,3]
# 输出：3
# 示例 2：
# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2
import collections
import random


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """哈希表"""
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement2(self, nums: list[int]) -> int:
        """排序"""
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement3(self, nums: list[int]) -> int:
        """随机化：由于一个给定的下标对应的数字很有可能是众数，我们随机挑选一个下标，检查它是否是众数，如果是就返回，否则继续随机挑选。"""
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate

    def majorityElement4(self, nums: list[int]) -> int:
        """分治：如果数 a 是数组 nums 的众数，如果我们将 nums 分成两部分，那么 a 必定是至少一部分的众数。"""

        def majority_element_rec(lo, hi) -> int:
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)

    def majorityElement5(self, nums: list[int]) -> int:
        """方法五：Boyer-Moore 投票算法：
        思路：如果我们把众数记为 +1，把其他数记为 −1，将它们全部加起来，显然和大于 0，从结果本身我们可以看出众数比其他数多。"""
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate


if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(s.majorityElement(nums))
    print(s.majorityElement2(nums))
    print(s.majorityElement3(nums))
    print(s.majorityElement4(nums))
    print(s.majorityElement5(nums))
