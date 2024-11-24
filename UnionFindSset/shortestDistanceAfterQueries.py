#
# * 3244. 新增道路查询后的最短距离 II - H
# 给你一个整数 n 和一个二维整数数组 queries。
# 有 n 个城市，编号从 0 到 n - 1。初始时，每个城市 i 都有一条单向道路通往城市 i + 1（ 0 <= i < n - 1）。
# queries[i] = [ui, vi] 表示新建一条从城市 ui 到城市 vi 的单向道路。每次查询后，你需要找到从城市 0 到城市 n - 1 的最短路径的长度。
# 所有查询中不会存在两个查询都满足 queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]。
# 返回一个数组 answer，对于范围 [0, queries.length - 1] 中的每个 i，answer[i] 是处理完前 i + 1 个查询后，从城市 0 到城市 n - 1 的最短路径的长度。

from typing import List


class UF:
    """并查集"""

    def __init__(self, n):
        self.father = list(range(n))
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
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        """
        用并查集实现边的合并。初始化一个大小为 n−1 的并查集，并查集中的节点 i 表示题目的边 i→(i+1)。（相当于给每条边编号 0,1,2,…n−2。）
        连一条从 L 到 R 的边，相当于把并查集中的节点 L,L+1,L+2⋯,R−2 合并到并查集中的节点 R−1 上。
        合并的同时，维护并查集连通块个数。
        答案就是每次合并后的并查集连通块个数
        """
        uf = UF(n - 1)
        ans = [0] * len(queries)
        for idx, (l, r) in enumerate(queries):
            fr = uf.find(r - 1)
            i = uf.find(l)
            while i < r - 1:
                uf.union(i, fr)
                i = uf.find(i + 1)
            ans[idx] = uf.sets
        return ans

    def shortestDistanceAfterQueries2(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        """
        定义 nxt[i] 表示 i 指向的最右节点编号，这里 0≤i≤n−2。
        初始值 nxt[i]=i+1。
        连一条从 L 到 R 的边，分类讨论：
        如果之前连了一条从 L′到 R′的边，且区间 [L,R] 被 [L′,R′] 包含，则什么也不做。
        否则更新 nxt[L]=R，在更新前，标记 [nxt[L],R−1] 中的没有被标记的点，表示这些点被更大的区间包含。怎么标记？
        
        把 nxt[i] 置为 0。和方法一一样，维护一个 cnt 变量，每把一个 nxt[i] 置为 0，就把 cnt 减一。
        也可以把 nxt[i] 置为 r，这样可以把进入循环和继续循环的逻辑合并成一个：当 nxt[i]<r 时进入循环/继续循环。
        """
        ans = []
        nxt = list(range(1, n))
        cnt = n - 1
        for l, r in queries:
            while nxt[l] < r:
                cnt -= 1
                l = nxt[l]
                nxt[l] = r
            ans.append(cnt)
        return ans


if __name__ == "__main__":
    sol = Solution()
    n = 5
    queries = [[2, 4], [0, 2], [0, 4]]
    print(sol.shortestDistanceAfterQueries(n, queries))
    print(sol.shortestDistanceAfterQueries2(n, queries))
