#
# * 407. 接雨水 II - H
# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水
# 示例:
# 输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# 输出: 10
import heapq


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        """时间复杂度：O(MNlog(MN))，其中 M 是矩阵的行数，N 是矩阵的列数。
        空间复杂度：O(MN)"""
        n, m = len(heightMap), len(heightMap[0])
        visited = [[False] * m for _ in range(n)]
        heap = []
        heapq.heapify(heap)
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        ans = 0
        # 根据木桶原理，接到的雨水的高度由这个容器周围最短的木板来确定的
        # 我们假设已经知道最外层的方块接水后的高度的最小值，则此时我们根据木桶原理，肯定可以确定最小高度方块的相邻方块的接水高度。
        # 我们同时更新最外层的方块标记，我们在新的最外层的方块再次找到接水后的高度的最小值，同时确定与其相邻的方块的接水高度
        # 然后再次更新最外层，依次迭代直到求出所有的方块的接水高度，即可知道矩阵中的接水容量。

        # 小根堆 按照 当前格子的 接水后的高度的排序，每次都计算水线高度最低的格子的水量，这样做不会漏掉水
        while heap:
            w, r, c = heapq.heappop(heap)
            ans += w - heightMap[r][c]
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    heapq.heappush(heap, (max(w, heightMap[nr][nc]), nr, nc))
                    visited[nr][nc] = True
        return ans
