#
# * 1162. 地图分析 * M
# 你现在手里有一份大小为 n x n 的 网格 grid，上面的每个 单元格 都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地。
# 请你找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的，并返回该距离。如果网格上只有陆地或者海洋，请返回 -1。
# 我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 - x1| + |y0 - y1| 。
from collections import deque


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        """时间复杂度: O(n*m)"""
        n, m = len(grid), len(grid[0])

        visited = [[False] * m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j))
                    visited[i][j] = True
        if len(q) == n * m or len(q) == 0:
            return -1

        level = 0
        while q:
            level += 1
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy]:
                        q.append((dx, dy))
                        visited[dx][dy] = True
        return level - 1


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    print(sol.maxDistance(grid))
