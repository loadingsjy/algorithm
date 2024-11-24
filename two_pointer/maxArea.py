#
# * 11. 盛最多水的容器 - M
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 返回容器可以储存的最大水量。
# 说明：你不能倾斜容器。


class Solution:
    def maxArea(self, height: list[int]) -> int:
        """双指针法"""
        ans = 0
        n = len(height)
        left = 0
        right = n - 1
        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(sol.maxArea(height))
