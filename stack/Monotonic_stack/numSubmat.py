# * 1504. 统计全 1 子矩形 - M
# 给你一个 m x n 的二进制矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。

# 示例 1：
# 输入：mat = [[1,0,1],[1,1,0],[1,1,0]]
# 输出：13
# 解释：
# 有 6 个 1x1 的矩形。
# 有 2 个 1x2 的矩形。
# 有 3 个 2x1 的矩形。
# 有 1 个 2x2 的矩形。
# 有 1 个 3x1 的矩形。
# 矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。
# 示例 2：
# 输入：mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
# 输出：24
# 解释：
# 有 8 个 1x1 的子矩形。
# 有 5 个 1x2 的子矩形。
# 有 2 个 1x3 的子矩形。
# 有 4 个 2x1 的子矩形。
# 有 2 个 2x2 的子矩形。
# 有 2 个 3x1 的子矩形。
# 有 1 个 3x2 的子矩形。
# 矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。
from copy import deepcopy


class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        """分别统计必须以每行为底的矩形数量"""
        n, m = len(mat), len(mat[0])
        ans = 0
        ans = self.CountRectangle(mat[0])
        for i in range(1, n):
            for j in range(m):
                if mat[i][j] == 1:
                    mat[i][j] += mat[i - 1][j]
            ans += self.CountRectangle(mat[i])
        return ans

    def CountRectangle(self, heights: list[int]) -> int:
        """
        比如:
                    1
                    1
                    1         1
        1         1         1
        1         1         1
        1         1         1

        3  ....   6   ....  8
        left      cur        i
        如上图，假设6位置从栈中弹出，6位置的高度为6(上面6个1)
        6位置的左边、离6位置最近、且小于高度6的是3位置(left)，3位置的高度是3
        6位置的右边、离6位置最近、且小于高度6的是8位置(i)，8位置的高度是4
        此时我们求什么？
        1) 求在4~7范围上必须以高度6作为高的矩形有几个？
        2) 求在4~7范围上必须以高度5作为高的矩形有几个？
        也就是说，<=4的高度一律不求，>6的高度一律不求！
        其他位置也会从栈里弹出，等其他位置弹出的时候去求！
        那么在4~7范围上必须以高度6作为高的矩形有几个？如下：
        4..4  4..5  4..6  4..7
        5..5  5..6  5..7
        6..6  6..7
        7..7
        10个！什么公式？
        4...7范围的长度为4，那么数量就是 : 4*5/2
        同理在4~7范围上，必须以高度5作为高的矩形也是这么多
        所以cur从栈里弹出时产生的数量 :
        (cur位置的高度-Max{left位置的高度,i位置的高度}) * ((i-left-1)*(i-left)/2)
        """
        """单调栈:求必须以底边为底的矩形数量"""
        n = len(heights)
        left = [-1] * n  # left[i]表示 左边最近比arr[i]小的index
        right = [n] * n

        stack = []
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                right[stack.pop()] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        ans = 0
        for i, h in enumerate(heights):
            left_h = heights[left[i]] if left[i] != -1 else 0
            right_h = heights[right[i]] if right[i] != n else 0
            bottem = h - max(left_h, right_h)
            width = right[i] - left[i] - 1
            ans += bottem * width * (width + 1) // 2

        return ans

    def numSubmat2(self, mat: list[list[int]]) -> int:
        """枚举"""
        n, m = len(mat), len(mat[0])

        row = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if j == 0:
                    row[i][j] = mat[i][j]
                else:
                    row[i][j] = 0 if mat[i][j] == 0 else row[i][j - 1] + 1

        ans = 0
        for i in range(n):
            for j in range(m):
                col = row[i][j]
                for k in range(i, -1, -1):
                    col = min(col, row[k][j])
                    if col == 0:
                        break
                    ans += col

        return ans


if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
    print(sol.numSubmat(deepcopy(mat)))
    print(sol.numSubmat2(mat))

    mat = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]
    print(sol.numSubmat(deepcopy(mat)))
    print(sol.numSubmat2(mat))
