#
# * 542. 01 矩阵 - M
# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
# 两个相邻元素间的距离为 1

# 提示：
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# mat 中至少有一个 0

from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        distances = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    distances[i][j] = float("inf")
        # 将所有的 0 添加进初始队列中
        q = deque(zeroes_pos)
        # seen = set(zeroes_pos)

        # 广度优先搜索
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n:
                    if distances[i][j] + 1 < distances[ni][nj]:
                        distances[ni][nj] = distances[i][j] + 1
                        q.append((ni, nj))
                        # seen.add((ni, nj))
        return distances


if __name__ == "__main__":
    sol = Solution()
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]

    print(sol.updateMatrix(mat))
