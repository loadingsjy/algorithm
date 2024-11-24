#
# * 1755. 最接近目标值的子序列和 - H

# 给你一个整数数组 nums 和一个目标值 goal 。
# 你需要从 nums 中选出一个子序列，使子序列元素总和最接近 goal 。也就是说，如果子序列元素和为 sum ，你需要 最小化绝对差 abs(sum - goal) 。
# 返回 abs(sum - goal) 可能的 最小值 。
# 注意，数组的子序列是通过移除原始数组中的某些元素（可能全部或无）而形成的数组。

# 示例 1：
# 输入：nums = [5,-7,3,5], goal = 6
# 输出：0
# 解释：选择整个数组作为选出的子序列，元素和为 6 。
# 子序列和与目标值相等，所以绝对差为 0 。
# 示例 2：
# 输入：nums = [7,-9,15,-2], goal = -5
# 输出：1
# 解释：选出子序列 [7,-9,-2] ，元素和为 -4 。
# 绝对差为 abs(-4 - (-5)) = abs(1) = 1 ，是可能的最小值。
# 示例 3：
# 输入：nums = [1,2,3], goal = -7
# 输出：7

# 提示：
# 1 <= nums.length <= 40
# -10^7 <= nums[i] <= 10^7
# -10^9 <= goal <= 10^9


class Solution:
    def minAbsDifference(self, nums: list[int], goal: int) -> int:
        n = len(nums)
        positive_sum = 0
        negative_sum = 0
        for num in nums:
            if num >= 0:
                positive_sum += num
            else:
                negative_sum += num

        if positive_sum <= goal:
            return goal - positive_sum
        if negative_sum >= goal:
            return negative_sum - goal

        nums.sort()

        # 从start开始到end，计算每个子序列的累加和，结果加入到path
        def dfs(start, end, sum_, path):
            if start == end:
                path.append(sum_)
                return
            j = start + 1
            while j < end and nums[j] == nums[start]:
                j += 1
            for k in range(j - start + 1):
                dfs(j, end, sum_ + k * nums[start], path)

        left_res = []
        dfs(0, n >> 1, 0, left_res)
        left_res.sort()

        right_res = []
        dfs(n >> 1, n, 0, right_res)
        right_res.sort()

        ans = abs(goal)
        i, j = 0, len(right_res) - 1
        # 滑动窗口
        while i < len(left_res):
            while j > 0 and abs(goal - left_res[i] - right_res[j - 1]) <= abs(
                goal - left_res[i] - right_res[j]
            ):
                j -= 1
            ans = min(ans, abs(goal - left_res[i] - right_res[j]))
            i += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [5, -7, 3, 5]
    goal = 6
    print(sol.minAbsDifference(nums, goal))
