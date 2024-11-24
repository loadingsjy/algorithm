#
# https://www.luogu.com.cn/problem/P3366
# P3366 【模板】最小生成树
# 如题，给出一个无向图，求出最小生成树，如果该图不连通，则输出 orz。

import sys


class UF:
    """并查集"""

    def __init__(self, n):
        self.father = [i for i in range(n + 1)]

    def find(self, i):
        if i != self.father[i]:
            self.father[i] = self.find(self.father[i])
        return self.father[i]

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx == fy:
            return False
        self.father[fx] = fy
        return True


def kruskal(n, edges):
    """kruskal 最小生成树算法  时间复杂度O(m * log m) + O(n) + O(m)
    1 把所有的边，根据权值从小到大排序，从权值小的边开始考虑
    2 如果连接当前的边不会形成环，就选择当前的边
    3 如果连接当前的边会形成环，就不要当前的边
    4 考察完所有边之后，最小生成树的也就得到了
    """
    uf = UF(n)
    edges.sort(key=lambda x: x[2])
    nodes_count = 1
    ans = 0
    for u, v, w in edges:
        if uf.union(u, v):  # 两个点在一个集合不能合并，否则会形成环
            ans += w
            nodes_count += 1
    return ans if nodes_count == n else "orz"


if __name__ == "__main__":
    line = input().split()
    n, m = int(line[0]), int(line[1])  # 点数量和边数量
    edges = []
    for line in sys.stdin:
        f, t, w = line.split()
        edges.append([int(f), int(t), int(w)])
    print(kruskal(n, edges))
