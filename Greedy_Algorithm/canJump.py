#
# * 55. 跳跃游戏

# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

# 示例 1：
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
# 示例 2：

# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
from functools import cache


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)

        @cache
        def dfs(i):
            if i >= n - 1:
                return True
            if nums[i] == 0 and i != n - 1:
                return False
            for j in range(1, nums[i] + 1):
                if dfs(i + j):
                    return True
            return False

        return dfs(0)

    def canJump2(self, nums: list[int]) -> bool:
        """贪心算法：这样以来，我们依次遍历数组中的每一个位置，并实时维护 最远可以到达的位置。
        对于当前遍历到的位置 x，如果它在 最远可以到达的位置 的范围内，那么我们就可以从起点通过若干次跳跃到达该位置，因此我们可以用 x+nums[x] 更新 最远可以到达的位置。
        在遍历的过程中，如果 最远可以到达的位置 大于等于数组中的最后一个位置，那就说明最后一个位置可达，我们就可以直接返回 True 作为答案。
        反之，如果在遍历结束后，最后一个位置仍然不可达，我们就返回 False 作为答案。"""
        n = len(nums)
        max_reach = 0  # 当前最远能到达的位置
        for i in range(n):
            if max_reach >= i:  # 当前位置能到
                max_reach = max(max_reach, i + nums[i])
            if max_reach >= n - 1:
                return True
        return False

    def canJump3(self, nums):
        n = len(nums)
        step = 1  # 走到目标需要的步数
        for i in range(n - 2, -1, -1):
            if nums[i] >= step:
                # 如果>=，代表从此元素可以达到
                step = 0
            step += 1
        return step == 1


if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    print(s.canJump2(nums))
    print(s.canJump3(nums))
