#
# * 827. 最大人工岛 - H

# 给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。
# 返回执行此操作后，grid 中最大的岛屿面积是多少？
# 岛屿 由一组上、下、左、右四个方向相连的 1 形成。

# 示例 1:
# 输入: grid = [[1, 0], [0, 1]]
# 输出: 3
# 解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
# 示例 2:
# 输入: grid = [[1, 1], [1, 0]]
# 输出: 4
# 解释: 将一格0变成1，岛屿的面积扩大为 4。
# 示例 3:
# 输入: grid = [[1, 1], [1, 1]]
# 输出: 4
# 解释: 没有0可以让我们变成1，面积依然为 4。

# 提示：
# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] 为 0 或 1

from collections import defaultdict
from copy import deepcopy


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        """先求出每个连通区域的面积（并编号，用哈希表存储），
        再遍历每个0位置，计算把他上下左右连通区域合并后的面积，取最大值"""
        n, m = len(grid), len(grid[0])

        def dfs(x, y, idx):
            """深度优先遍历，将遍历到的连通区域设置为id，并计算整个连通区域的面积"""
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 1:
                return 0
            grid[x][y] = idx
            eara = 0
            eara += (
                dfs(x - 1, y, idx)
                + dfs(x + 1, y, idx)
                + dfs(x, y - 1, idx)
                + dfs(x, y + 1, idx)
                + 1
            )
            return eara

        ans = 0
        eara_cnts = defaultdict(int)
        idx = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    eara_cnts[idx] = dfs(i, j, idx)
                    ans = max(ans, eara_cnts[idx])
                    idx += 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    up = grid[i - 1][j] if i > 0 else 0
                    down = grid[i + 1][j] if i + 1 < n else 0
                    left = grid[i][j - 1] if j > 0 else 0
                    right = grid[i][j + 1] if j + 1 < m else 0
                    merge = 1
                    for index in set([up, down, left, right]):
                        merge += eara_cnts[index]
                    ans = max(ans, merge)
        return ans

    def largestIsland2(self, grid: list[list[int]]) -> int:
        """灵神写法"""
        n = len(grid)

        def dfs(i: int, j: int) -> int:
            size = 1
            grid[i][j] = len(area) + 2  # 记录 (i,j) 属于哪个岛
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    size += dfs(x, y)
            return size

        # DFS 每个岛，统计各个岛的面积，记录到 area 列表中
        area = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    area.append(dfs(i, j))

        # 加上这个特判，可以快很多
        if not area:  # 没有岛
            return 1

        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    continue
                s = set()
                for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if 0 <= x < n and 0 <= y < n and grid[x][y]:
                        s.add(grid[x][y])  # 记录上下左右格子所属岛屿编号
                ans = max(ans, sum(area[idx - 2] for idx in s) + 1)  # 累加面积

        # 如果最后 ans 仍然为 0，说明所有格子都是 1，返回 n^2
        return ans if ans else n * n


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 0], [0, 1]]
    print(sol.largestIsland(deepcopy(grid)))
    print(sol.largestIsland2(deepcopy(grid)))
