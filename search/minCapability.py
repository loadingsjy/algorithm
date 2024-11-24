#
# * 2560. 打家劫舍 IV - M
# 沿街有一排连续的房屋。每间房屋内都藏有一定的现金。现在有一位小偷计划从这些房屋中窃取现金。
# 由于相邻的房屋装有相互连通的防盗系统，所以小偷 不会窃取相邻的房屋 。
# 小偷的 窃取能力 定义为他在窃取过程中能从单间房屋中窃取的 最大金额 。
# 给你一个整数数组 nums 表示每间房屋存放的现金金额。形式上，从左起第 i 间房屋中放有 nums[i] 美元。
# 另给你一个整数 k ，表示窃贼将会窃取的 最少 房屋数。小偷总能窃取至少 k 间房屋。
# 返回小偷的 最小 窃取能力。

# 示例 1：
# 输入：nums = [2,3,5,9], k = 2
# 输出：5
# 解释：
# 小偷窃取至少 2 间房屋，共有 3 种方式：
# - 窃取下标 0 和 2 处的房屋，窃取能力为 max(nums[0], nums[2]) = 5 。
# - 窃取下标 0 和 3 处的房屋，窃取能力为 max(nums[0], nums[3]) = 9 。
# - 窃取下标 1 和 3 处的房屋，窃取能力为 max(nums[1], nums[3]) = 9 。
# 因此，返回 min(5, 9, 9) = 5 。
# 示例 2：
# 输入：nums = [2,7,9,3,1], k = 2
# 输出：2
# 解释：共有 7 种窃取方式。窃取能力最小的情况所对应的方式是窃取下标 0 和 4 处的房屋。返回 max(nums[0], nums[4]) = 2 。

# 提示：
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= (nums.length + 1)/2


class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        """二分答案法 + 动态规划"""
        n = len(nums)

        # def count(ability):
        #     """动态规划"""
        #     if n == 1:
        #         return int(nums[0] <= ability)
        #     if n == 2:
        #         return int(nums[0] <= ability or nums[1] <= ability)
        #     # dp[i] 表示偷窃到第 i 个房屋的最大金额(包含第 i 个房屋)
        #     dp = [0] * n
        #     dp[0] = int(nums[0] <= ability)
        #     dp[1] = int(nums[0] <= ability or nums[1] <= ability)
        #     for i in range(2, n):
        #         dp[i] = max(dp[i - 1], dp[i - 2] + int(nums[i] <= ability))
        #     return dp[-1]

        # def count(ability):
        #     """动态规划 空间优化"""
        #     if n == 1:
        #         return int(nums[0] <= ability)
        #     if n == 2:
        #         return int(nums[0] <= ability or nums[1] <= ability)
        #     prev_prev = int(nums[0] <= ability)
        #     prev = int(nums[0] <= ability or nums[1] <= ability)
        #     for i in range(2, n):
        #         cur = max(prev, prev_prev + int(nums[i] <= ability))
        #         prev_prev, prev = prev, cur
        #     return cur

        def count(ability):
            """贪心算法"""
            ans = 0
            i = 0
            while i < n:
                if nums[i] <= ability:
                    ans += 1
                    i += 2
                else:
                    i += 1
            return ans

        l, r = min(nums), max(nums)
        while l <= r:
            mid = (l + r) // 2
            if count(mid) >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l
