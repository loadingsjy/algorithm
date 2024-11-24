#
# * 2779. 数组的最大美丽值 - M
# 给你一个下标从 0 开始的整数数组 nums 和一个 非负 整数 k 。
# 在一步操作中，你可以执行下述指令：
# 在范围 [0, nums.length - 1] 中选择一个 此前没有选过 的下标 i 。
# 将 nums[i] 替换为范围 [nums[i] - k, nums[i] + k] 内的任一整数。
# 数组的 美丽值 定义为数组中由相等元素组成的最长子序列的长度。
# 对数组 nums 执行上述操作任意次后，返回数组可能取得的 最大 美丽值。
# 注意：你 只 能对每个下标执行 一次 此操作。
# 数组的 子序列 定义是：经由原数组删除一些元素（也可能不删除）得到的一个新数组，且在此过程中剩余元素的顺序不发生改变。

# 示例 1：
# 输入：nums = [4,6,1,2], k = 2
# 输出：3
# 解释：在这个示例中，我们执行下述操作：
# - 选择下标 1 ，将其替换为 4（从范围 [4,8] 中选出），此时 nums = [4,4,1,2] 。
# - 选择下标 3 ，将其替换为 4（从范围 [0,4] 中选出），此时 nums = [4,4,1,4] 。
# 执行上述操作后，数组的美丽值是 3（子序列由下标 0 、1 、3 对应的元素组成）。
# 可以证明 3 是我们可以得到的由相等元素组成的最长子序列长度。
# 示例 2：
# 输入：nums = [1,1,1,1], k = 10
# 输出：4
# 解释：在这个示例中，我们无需执行任何操作。
# 数组 nums 的美丽值是 4（整个数组）。

# 提示：
# 1 <= nums.length <= 105
# 0 <= nums[i], k <= 105

from itertools import accumulate


class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        """排序+二分答案 时间复杂度O(nlogn)"""
        nums.sort()
        n = len(nums)

        def check(b):
            """返回数组能否进行多次指令，最大美丽值为b"""
            for i in range(0, n - b + 1):
                if nums[i + b - 1] - nums[i] <= 2 * k:
                    return True
            return False

        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r

    def maximumBeauty2(self, nums: list[int], k: int) -> int:
        """排序+滑动窗口 时间复杂度O(nlogn)+O(n)"""
        nums.sort()
        left = 0
        ans = 0
        for right, num in enumerate(nums):
            while left <= right and num - nums[left] > 2 * k:
                left += 1
            ans = max(ans, right - left + 1)
        return ans

    def maximumBeauty3(self, nums: list[int], k: int) -> int:
        """差分数组:
        第i个数能给[nums[i] - k, nums[i] + k]区间中的每个数各投一票，最终票数最多的那个就是答案。
        投票过程相当于给一个数组区间的元素各+1，这样就自然地想到差分数组了。
        时间复杂度：O(n+m),n为数组长度，m为数组最大值"""
        m = max(nums)
        diff = [0] * (m + 2)
        for x in nums:
            diff[max(x - k, 0)] += 1
            diff[min(x + k + 1, m + 1)] -= 1
        res, count = 0, 0
        for x in diff:
            count += x
            res = max(res, count)
        return res

    def maximumBeauty4(self, nums: list[int], k: int) -> int:
        """差分数组 最快最简写法"""
        m = max(nums) + k * 2 + 2
        d = [0] * m
        for x in nums:
            d[x] += 1
            d[x + k * 2 + 1] -= 1
        return max(accumulate(d))


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 6, 1, 2]
    k = 2
    print(sol.maximumBeauty(nums, k))
    print(sol.maximumBeauty2(nums, k))
    print(sol.maximumBeauty3(nums, k))
    print(sol.maximumBeauty4(nums, k))
