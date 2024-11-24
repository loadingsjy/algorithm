#
# https://www.luogu.com.cn/problem/P3366
# P3366 【模板】最小生成树
# 如题，给出一个无向图，求出最小生成树，如果该图不连通，则输出 orz。

import sys, heapq
from collections import defaultdict


def prim(n, edges):
    """prim 最小生成树算法 时间复杂度O(n + m) + O(m * log m)"""

    next_nodes = defaultdict(list)
    for u, v, w in edges:
        next_nodes[u].append((v, w))
        next_nodes[v].append((u, w))

    nodes_set = [False] * (n + 1)
    heap = []
    heapq.heapify(heap)
    for nxt, w in next_nodes[1]:
        heapq.heappush(heap, (w, nxt))
    node_count = 1
    nodes_set[1] = True
    ans = 0
    while heap:
        w, node = heapq.heappop(heap)
        if not nodes_set[node]:
            node_count += 1
            nodes_set[node] = True
            ans += w
            for nxt, w in next_nodes[node]:
                heapq.heappush(heap, (w, nxt))
    return ans if node_count == n else "orz"


if __name__ == "__main__":
    line = input().split()
    n, m = int(line[0]), int(line[1])  # 点数量和边数量
    edges = []
    for line in sys.stdin:
        if not line.strip():
            break
        f, t, w = line.split()
        edges.append([int(f), int(t), int(w)])
    print(prim(n, edges))
