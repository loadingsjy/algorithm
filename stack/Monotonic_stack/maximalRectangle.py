#
# * 85. 最大矩形 - H
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。


class Solution:

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        """首先对矩阵的每个位置构建前缀连续1的数量矩阵，对矩阵中的每一列求柱状图能构成的最大面积。
        同理可以对每行求最大矩阵的面积"""
        n, m = len(matrix), len(matrix[0])
        matrix = [list(map(int, row)) for row in matrix]  # 将矩阵中字符转为数字
        ans = self.largestRectangleArea(matrix[0])
        for i in range(1, n):
            for j in range(m):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]
            ans = max(ans, self.largestRectangleArea(matrix[i]))
        return ans

    def largestRectangleArea(self, heights: list[int]) -> int:
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
    sol = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    print(sol.maximalRectangle(matrix))
