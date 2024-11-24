#
# * 947. 移除最多的同行或同列石头 - M
# n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。
# 如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。
# 给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。

# 示例 1：
# 输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# 输出：5
# 解释：一种移除 5 块石头的方法如下所示：
# 1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
# 2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
# 3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
# 4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
# 5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
# 石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。
# 示例 2：
# 输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# 输出：3
# 解释：一种移除 3 块石头的方法如下所示：
# 1. 移除石头 [2,2] ，因为它和 [2,0] 同行。
# 2. 移除石头 [2,0] ，因为它和 [0,0] 同列。
# 3. 移除石头 [0,2] ，因为它和 [0,0] 同行。
# 石头 [0,0] 和 [1,1] 不能移除，因为它们没有与另一块石头同行/列。
# 示例 3：
# 输入：stones = [[0,0]]
# 输出：0
# 解释：[0,0] 是平面上唯一一块石头，所以不可以移除它。

# 提示：
# 1 <= stones.length <= 1000
# 0 <= xi, yi <= 104
# 不会有两块石头放在同一个坐标点上


class UF:
    """并查集"""

    def __init__(self, n):
        self.father = [i for i in range(n)]
        self.sets = n  # 集合数量

    def find(self, i):
        if i != self.father[i]:
            self.father[i] = self.find(self.father[i])
        return self.father[i]

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.father[fx] = fy
            self.sets -= 1


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        """结论：一个集团的石头(n)个最多可以移除n-1个石，最后只剩下一个石头
        (最优方法：从边缘开始移除，肯定最后只剩下一块石头)"""
        row_dict = dict()  # key:行号，value:该行第一个出现石头的编号
        col_dict = dict()  # key:列号，value:该列第一个出现石头的编号
        n = len(stones)
        uf = UF(n)
        for i, (r, c) in enumerate(stones):
            if r in row_dict:
                uf.union(i, row_dict[r])
            else:
                row_dict[r] = i
            if c in col_dict:
                uf.union(i, col_dict[c])
            else:
                col_dict[c] = i
        return n - uf.sets


if __name__ == "__main__":
    sol = Solution()
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    print(sol.removeStones(stones))
