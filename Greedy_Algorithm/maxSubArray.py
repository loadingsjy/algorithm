# 53. 最大子数组和

# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组是数组中的一个连续部分。


# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 示例 2：
# 输入：nums = [1]
# 输出：1
# 示例 3：
# 输入：nums = [5,4,-1,7,8]
# 输出：23
from math import inf


class Solution:

    def maxSubArray(self, nums: list[int]) -> int:
        """求前缀和的最小值：
        我们可以一边遍历数组计算前缀和，一边维护前缀和的最小值（相当于股票最低价格），
        用当前的前缀和（卖出价格）减去前缀和的最小值（买入价格），就得到了以当前元素结尾的子数组和的最大值（利润），
        用它来更新答案的最大值（最大利润）。"""
        ans = -inf
        min_pre_sum = pre_sum = 0
        for x in nums:
            pre_sum += x  # 当前的前缀和
            ans = max(ans, pre_sum - min_pre_sum)  # 减去前缀和的最小值
            min_pre_sum = min(min_pre_sum, pre_sum)  # 维护前缀和的最小值
        return ans

    def maxSubArray2(self, nums: list[int]) -> int:
        """贪心算法: 若当前指针所指之前元素和<0，则丢弃掉当前元素之前的数列"""
        cur_sum = 0
        ans = -inf  # 注意答案可以是负数，不能初始化成 0
        for num in nums:
            if cur_sum < 0:
                cur_sum = num
            else:
                cur_sum = cur_sum + num
            ans = max(ans, cur_sum)
        return ans

    def maxSubArray3(self, nums: list[int]) -> int:
        """动态规划 原地修改数组"""
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)

    def maxSubArray4(self, nums: list[int]) -> int:
        """动态规划：定义 f[i] 表示必须以 nums[i] 结尾的最大子数组和。"""
        f = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i - 1], 0) + nums[i]
        return max(f)

    def maxSubArray4_improved(self, nums: list[int]) -> int:
        """由于计算 f[i] 只会用到 f[i−1]，不会用到更早的状态，所以可以用一个变量滚动计算。"""
        ans = -inf  # 注意答案可以是负数，不能初始化成 0
        f = 0
        for x in nums:
            f = max(f, 0) + x
            ans = max(ans, f)
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray(nums))
    print(s.maxSubArray2(nums))
    # print(s.maxSubArray3(nums))
    print(s.maxSubArray4(nums))
    print(s.maxSubArray4_improved(nums))
