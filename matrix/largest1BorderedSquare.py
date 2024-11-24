#
# * 1139. 最大的以 1 为边界的正方形 - H
# 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。

# 示例 1：
# 输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：9
# 示例 2：
# 输入：grid = [[1,1,0,0]]
# 输出：1

# 提示：
# 1 <= grid.length <= 100
# 1 <= grid[0].length <= 100
# grid[i][j] 为 0 或 1


class Solution:
    def largest1BorderedSquare(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def get(i, j):
            """特判越界情况"""
            return 0 if i < 0 or j < 0 else grid[i][j]

        def cal_sum(a, b, c, d):
            """计算(a,b)为左上角，(c,d)为右下角的矩阵累加和"""
            if a > c:
                return 0
            return grid[c][d] - get(a - 1, d) - get(c, b - 1) + get(a - 1, b - 1)

        def build(grid):
            """在grid矩阵本身上构建前缀和矩阵"""

            for i in range(1, n):
                grid[i][0] += grid[i - 1][0]
            for i in range(1, m):
                grid[0][i] += grid[0][i - 1]

            for i in range(1, n):
                for j in range(1, m):
                    grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1]

        build(grid)
        if cal_sum(0, 0, n - 1, m - 1) == 0:
            return 0
        ans = 1

        # 枚举所有的正方形右上角点和边长
        for a in range(n - 1):
            for b in range(m - 1):
                side = ans + 1  # 边长从 ans + 1 开始枚举，短边长没必要枚举了
                while a + side <= n and b + side <= m:
                    c = a + side - 1
                    d = b + side - 1
                    # 大正方形累加和 - 小正方形的累加和 等于 4*(k-1) 就意味着大正方形的边长都为1，符合题目要求
                    if cal_sum(a, b, c, d) - cal_sum(
                        a + 1, b + 1, c - 1, d - 1
                    ) == 4 * (side - 1):

                        ans = side
                    side += 1

        return ans * ans

    def largest1BorderedSquare2(self, grid):
        """动态规划预处理"""
        m, n = len(grid), len(grid[0])

        # left[x][y] 表示以 (x,y) 为起点左侧连续 1 的最大数目
        left = [[0] * (n + 1) for _ in range(m + 1)]
        # up[x][y] 表示从 (x,y) 为起点上方连续 1 的最大数目
        up = [[0] * (n + 1) for _ in range(m + 1)]

        maxBorder = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i - 1][j - 1]:
                    left[i][j] = left[i][j - 1] + 1
                    up[i][j] = up[i - 1][j] + 1
                    border = min(left[i][j], up[i][j])
                    # 从最大可能边长开始枚举
                    while (
                        left[i - border + 1][j] < border
                        or up[i][j - border + 1] < border
                    ):
                        border -= 1
                    maxBorder = max(maxBorder, border)
        return maxBorder**2
