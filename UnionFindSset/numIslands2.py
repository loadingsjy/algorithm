#
# * 305. 岛屿数量 II - H
# 给你一个大小为 m x n 的二维二进制网格 grid 。网格表示一个地图，其中，0 表示水，1 表示陆地。
# 最初，grid 中的所有单元格都是水单元格（即，所有单元格都是 0）。
# 可以通过执行 addLand 操作，将某个位置的水转换成陆地。
# 给你一个数组 positions ，其中 positions[i] = [ri, ci] 是要执行第 i 次操作的位置 (ri, ci) 。
# 返回一个整数数组 answer ，其中 answer[i] 是将单元格 (ri, ci) 转换为陆地后，地图中岛屿的数量。
# 岛屿 的定义是被「水」包围的「陆地」，通过水平方向或者垂直方向上相邻的陆地连接而成。你可以假设地图网格的四边均被无边无际的「水」所包围。

# 示例 1:
# 输入：m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
# 输出：[1,1,2,3]
# 解释：
# 起初，二维网格 grid 被全部注入「水」。（0 代表「水」，1 代表「陆地」）
# - 操作 #1：addLand(0, 0) 将 grid[0][0] 的水变为陆地。此时存在 1 个岛屿。
# - 操作 #2：addLand(0, 1) 将 grid[0][1] 的水变为陆地。此时存在 1 个岛屿。
# - 操作 #3：addLand(1, 2) 将 grid[1][2] 的水变为陆地。此时存在 2 个岛屿。
# - 操作 #4：addLand(2, 1) 将 grid[2][1] 的水变为陆地。此时存在 3 个岛屿。
# 示例 2：
# 输入：m = 1, n = 1, positions = [[0,0]]
# 输出：[1]


class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        if x == y:
            return
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.p[rx] = ry


class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        """并查集三个功能：1.寻找集合根 2.合并 3.初始化
        思路：
        1.初始化m * n个点的并查集空间， 初始化没有任何集合 count = 0
        2.当传进新的点时
            1)count += 1
            2)判断和周围在集合中的点是否有同样的根，有则合并，并count -= 1
        主要用并查集维护了count的数量，实际上在调整m * n图内的集合。
        """
        seen = set()
        uf = UF(m * n)
        count = 0
        res = []
        for pos in positions:
            x, y = pos
            if (x, y) in seen:
                res.append(count)
                continue
            idx = x * n + y
            seen.add((x, y))
            count += 1
            for dx, dy in (1, 0), (0, 1), (0, -1), (-1, 0):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if (nx, ny) not in seen:
                    continue
                idx2 = nx * n + ny
                rx = uf.find(idx)
                ry = uf.find(idx2)
                if rx != ry:
                    uf.union(idx, idx2)
                    count -= 1
            res.append(count)
        return res

    def numIslands2_2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        def find(node):
            while parent[node] != parent[parent[node]]:  # fixed points
                parent[node] = parent[parent[node]]
            return parent[node]

        def union(n1, n2):
            parent[find(n1)] = find(n2)  # n1代表合并到n2代表

        res = [0] * len(positions)
        parent = [i for i in range(m * n)]
        land = [0 for i in range(m * n)]
        for i, (r, c) in enumerate(positions):
            idx = r * n + c
            if land[idx]:  # 已经是陆地略过，res不变
                res[i] = res[i - 1]
                continue
            land[idx] = 1
            res[i] = res[i - 1] + 1  # 遇到新陆地先加1，假设是孤立点
            for dx, dy in (1, 0), (0, 1), (0, -1), (-1, 0):
                x, y = r + dx, c + dy
                if (
                    m > x >= 0 <= y < n
                    and land[x * n + y] == 1
                    and find(idx) != find(x * n + y)
                ):
                    union(idx, x * n + y)
                    res[i] -= 1  # 检查四周，发现相邻parent不一样就打通，并且res-1
        return res


if __name__ == "__main__":
    sol = Solution()
    m = 3
    n = 3
    positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
    print(sol.numIslands2(m, n, positions))
    print(sol.numIslands2_2(m, n, positions))
