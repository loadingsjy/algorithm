#
# * 1658. 将 x 减到 0 的最小操作数 - M

# 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。
# 如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。

# 示例 1：
# 输入：nums = [1,1,4,2,3], x = 5
# 输出：2
# 解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
# 示例 2：
# 输入：nums = [5,6,7,8,9], x = 4
# 输出：-1
# 示例 3：
# 输入：nums = [3,2,20,1,1,3], x = 10
# 输出：5
# 解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。

# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 1 <= x <= 10^9


class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        """转化为 数组总长度 - 子数组累加和为(total sum - x)的最大长度"""
        if min(nums) > x:
            return -1

        n = len(nums)
        target = sum(nums) - x

        if target < 0:
            return -1
        if target == 0:
            return n

        sum_ = 0
        left, ans = 0, -1
        for right, num in enumerate(nums):
            sum_ += num
            while left <= right and sum_ > target:
                sum_ -= nums[left]
                left += 1
            if sum_ == target:
                ans = max(ans, right - left + 1)
        if ans == -1:  # 没有这样的子数组
            return -1
        return n - ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 4, 2, 3]
    x = 5
    print(sol.minOperations(nums, x))

    nums = [5, 6, 7, 8, 9]
    x = 4
    print(sol.minOperations(nums, x))

    nums = [3, 2, 20, 1, 1, 3]
    x = 10
    print(sol.minOperations(nums, x))
