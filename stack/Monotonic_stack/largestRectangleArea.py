#
# * 84. 柱状图中最大的矩形 - M
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。

# 示例 1:
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
# 示例 2：
# 输入： heights = [2,4]
# 输出： 4


class Solution:

    def largestRectangleArea(self, heights: list[int]) -> int:
        """暴力法1: 先确定高度，在向两边扩散，找到最大面积
        暴力法2: 先遍历所有可能得底边，再找到底边范围内的最大高度"""
        pass

    def largestRectangleArea2(self, heights: list[int]) -> int:
        """单调栈（栈底小，栈顶大）：每次出栈时，求出当前高度能构成的最大矩形的面积"""
        n = len(heights)
        ans = heights[0]
        stack = []

        for i, h in enumerate(heights):
            while stack and h <= heights[stack[-1]]:
                cur_h = heights[stack.pop()]
                if not stack:  # 表示当前高度可以扩散到最左边
                    ans = max(ans, cur_h * i)
                    break
                left = stack[-1]
                ans = max(ans, cur_h * (i - left - 1))
            stack.append(i)

        while stack:  # 剩下的高度都可以扩散到最右边
            cur_h = heights[stack.pop()]
            if not stack:
                ans = max(ans, cur_h * n)
                break
            left = stack[-1]
            ans = max(ans, cur_h * (n - left - 1))

        return ans

    def largestRectangleArea3(self, heights: list[int]) -> int:
        # 单调递增栈，遇到一个较小的，可以算出前一个面积。宽需再次获取栈顶元素
        heights = [0] + heights + [0]  # 两边增加两个零，可以不用处理特殊情况

        stack = []
        ans = 0

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                # 对于重复元素，会多次求面积，最后会算到最大面积
                # [9,8,7,7,7,7,6]. 6这里会分别与前面四个7算出最大面积
                dh = heights[stack.pop()]
                dw = i - stack[-1] - 1
                ans = max(ans, dh * dw)

            stack.append(i)

        return ans

    def largestRectangleArea4(self, heights: list[int]) -> int:
        """单调栈：分别求出每个高度左边和右边最近小于当前高度的index"""
        n = len(heights)
        ans = heights[0]
        left = [-1] * n  # left[i]表示 左边最近比arr[i]小的index
        right = [n] * n

        stack = []
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                right[stack.pop()] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        for i, h in enumerate(heights):
            ans = max(ans, h * (right[i] - left[i] - 1))

        return ans


if __name__ == "__main__":
    s = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    # print(s.largestRectangleArea(heights))
    print(s.largestRectangleArea2(heights))
    print(s.largestRectangleArea3(heights))
    print(s.largestRectangleArea4(heights))
