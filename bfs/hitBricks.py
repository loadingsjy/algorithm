#
# * 803. 打砖块 - H
# 有一个 m x n 的二元网格 grid ，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：
# 一块砖直接连接到网格的顶部，或者
# 至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时
# 给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli) 位置上的砖块时，
# 对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而 掉落 。
# 一旦砖块掉落，它会 立即 从网格 grid 中消失（即，它不会落在其他稳定的砖块上）。
# 返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。
# 注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。

# 示例 1：
# 输入：grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
# 输出：[2]
# 解释：网格开始为：
# [[1,0,0,0]，
#  [1,1,1,0]]
# 消除 (1,0) 处加粗的砖块，得到网格：
# [[1,0,0,0]
#  [0,1,1,0]]
# 两个加粗的砖不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格：
# [[1,0,0,0],
#  [0,0,0,0]]
# 因此，结果为 [2] 。

# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[i][j] 为 0 或 1
# 1 <= hits.length <= 4 * 104
# hits[i].length == 2
# 0 <= xi <= m - 1
# 0 <= yi <= n - 1
# 所有 (xi, yi) 互不相同


class Solution:
    def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        """基本流程：
        1) 炮弹位置的数值 -1
        2) 天花板(顶部)dfs都设置成 2
        3) 时光倒流：从最后一个炮弹开始，恢复值 并 dfs求出周围连通1的面积
        相当于先给路断了，然后在按照时间逆序恢复，这种技巧能保证后面击打的效果不受之前的影响
        """
        n, m = len(grid), len(grid[0])
        res = [0] * (l := len(hits))
        if n == 1:
            return res

        def dfs(x, y):
            """深度优先遍历，将连通区域的值设置为2，并返回面积"""
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 1:
                return 0
            grid[x][y] = 2
            eara = 0
            eara += dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1) + 1
            return eara

        def vaild(x, y):
            """返回当前位置是否为 有效击打的位置，两种情况：本身是天花板；周围连接天花板，即周围有2"""
            if grid[x][y] != 1:  # 原来是0，本来就是无效击打位置
                return False
            if x == 0:  # 本身是天花板
                return True
            values = set()
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < n and 0 <= j < m:
                    values.add(grid[i][j])
            return 2 in values  # 周围连接天花板，即周围有2

        for x, y in hits:
            grid[x][y] -= 1

        for i in range(m):  # 天花板感染
            if grid[0][i] == 1:
                dfs(0, i)

        for i in range(l - 1, -1, -1):
            x, y = hits[i]
            grid[x][y] += 1
            if vaild(x, y):  # 有效击打位置
                res[i] = dfs(x, y) - 1
        return res


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 0, 0, 0], [1, 1, 1, 0]]
    hits = [[1, 0]]
    print(sol.hitBricks(grid, hits))
