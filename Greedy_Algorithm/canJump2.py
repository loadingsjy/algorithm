#
# *45. 跳跃游戏 II

# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
# 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
# 0 <= j <= nums[i]
# i + j < n
# 返回到达 nums[n - 1] 的最小跳跃次数。题目保证可以到达 nums[n-1]。

# 示例 1:
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 示例 2:
# 输入: nums = [2,3,0,1,4]
# 输出: 2


from functools import cache


class Solution:
    def jump(self, nums: list[int]) -> int:
        """超时"""
        n = len(nums)
        ans = float("inf")

        def dfs(i, step):
            if i == n - 1:
                nonlocal ans
                ans = min(ans, step)
                return
            if nums[i] == 0 and i != n - 1:
                return
            for j in range(1, nums[i] + 1):
                dfs(i + j, step + 1)

        dfs(0, 0)
        return ans

    def jump2(self, nums: list[int]) -> bool:
        """贪心算法"""
        n = len(nums)
        max_reach = 0  # 当前最远能到达的位置
        min_step = [0] * n  # min_step[i]代表到达i位置所需要的最少步数
        for i in range(n):
            if max_reach >= n - 1:
                return min_step[-1]
            if max_reach >= i:  # 当前位置能到
                if i + nums[i] > max_reach:  # 可以跳到更远的距离
                    s = min_step[i]
                    for j in range(max_reach + 1, min(i + nums[i] + 1, n)):
                        min_step[j] = s + 1
                    max_reach = i + nums[i]

    def jump3(self, nums: list[int]) -> bool:
        n = len(nums)
        step = 0
        end = 0  # 当前步数范围内的最后一格
        maxPos = 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(nums[i] + i, maxPos)
                if i == end:  # 说明后面的格子要多走一步
                    end = maxPos
                    step += 1
        return step

    def jump4(self, nums):
        """反向查找出发位置：我们的目标是到达数组的最后一个位置，因此我们可以考虑最后一步跳跃前所在的位置，该位置通过跳跃能够到达最后一个位置。
        时间复杂度O(n^2)，不推荐"""
        position = len(nums) - 1
        steps = 0
        while position > 0:
            for i in range(position):
                if i + nums[i] >= position:
                    position = i
                    steps += 1
                    break
        return steps


if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    print(s.jump2(nums))
    print(s.jump3(nums))
    print(s.jump4(nums))
