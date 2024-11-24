#
# * 42. 接雨水 - H
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


class Solution:
    def trap(self, height: list[int]) -> int:
        """最大值前后缀法，时间复杂度：O(N)，空间复杂度O(N)"""

        n = len(height)
        pre_max = [0] * n
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        suf_max = [0] * n
        suf_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        ans = 0

        for h, p, s in zip(height, pre_max, suf_max):
            ans += max(0, min(p, s) - h)
        return ans

    def trap2(self, height: list[int]) -> int:
        """优化成双指针法，时间复杂度：O(N)，空间复杂度O(1)"""

        n = len(height)
        ans = 0
        pre_max = 0
        suf_max = 0
        left, right = 0, n - 1
        while left < right:
            pre_max = max(height[left], pre_max)
            suf_max = max(height[right], suf_max)
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans

    def trap3(self, height: list[int]) -> int:
        """单调栈法：找上一个更大的元素，找的过程中填坑， 每次出栈可以理解为从下到上横着填坑
        时间复杂度：O(N)，空间复杂度O(N)"""

        ans = 0
        stack = []
        for i, h in enumerate(height):
            while stack and h >= height[stack[-1]]:
                bottem_h = height[stack.pop()]
                if not stack:
                    break
                left = stack[-1]
                # 宽度 = 当前位置 - 当前栈顶位置 - 1
                # 高度 = 当前位置的高度和当前栈顶位置的高度取最小值 - 下面已经有的高度
                ans += (i - left - 1) * (min(h, height[left]) - bottem_h)
            stack.append(i)
        return ans


if __name__ == "__main__":
    s = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap(height))
    print(s.trap2(height))
    print(s.trap3(height))
