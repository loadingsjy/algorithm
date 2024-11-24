#
# * 743. 网络延迟时间 - M
# 有 n 个网络节点，标记为 1 到 n。
# 给你一个列表 times，表示信号经过 有向 边的传递时间。
# times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。
# 现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。
# 示例 1：
# 输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# 输出：2

# 提示：
# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# 所有 (ui, vi) 对都 互不相同（即，不含重复边）

from math import inf
from heapq import *
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """堆优化 Dijkstra算法（适用于稀疏图）  时间复杂度：O(mlogm)  空间复杂度：O(n+m)  n=点的数量，m=边的数量"""
        # 邻接表建图
        next_nodes = defaultdict(list)
        for u, v, w in times:
            next_nodes[u].append((v, w))

        distances = [inf] * (n + 1)
        distances[k] = 0
        visited = [False] * (n + 1)
        heap = [(0, k)]
        heapify(heap)
        while heap:
            w, cur = heappop(heap)
            if not visited[cur]:
                visited[cur] = True
                for nxt, w in next_nodes[cur]:
                    if not visited[nxt] and distances[cur] + w < distances[nxt]:
                        distances[nxt] = distances[cur] + w
                        heappush(heap, (distances[cur] + w, nxt))
        ans = max(distances[1:])
        if ans == inf:
            return -1
        return ans

    def networkDelayTime2(self, times: list[list[int]], n: int, k: int) -> int:
        """朴素 Dijkstra算法（适用于稠密图）    时间复杂度：O(n^2 + m)  空间复杂度：O(n^2)， n=点的数量，m=边的数量"""
        g = [[inf for _ in range(n)] for _ in range(n)]  # 邻接矩阵
        for x, y, d in times:
            g[x - 1][y - 1] = d

        dis = [inf] * n
        ans = dis[k - 1] = 0
        done = [False] * n
        while True:
            x = -1
            # 找到 [未确定] 结果的点中最小的结果，将他标为确定的结果
            for i, ok in enumerate(done):
                if not ok and (x < 0 or dis[i] < dis[x]):
                    x = i
            if x < 0:
                return ans  # 最后一次算出的最短路就是最大的
            if dis[x] == inf:  # 有节点无法到达
                return -1
            ans = dis[x]  # 求出的最短路会越来越大
            done[x] = True  # 最短路长度已确定（无法变得更小）
            for y, d in enumerate(g[x]):
                # 更新 x 的邻居的最短路
                dis[y] = min(dis[y], dis[x] + d)

    def networkDelayTime3(self, times: list[list[int]], n: int, k: int) -> int:
        """堆优化 Dijkstra算法  灵神写法：不用visited数组"""
        g = [[] for _ in range(n)]  # 邻接表
        for x, y, d in times:
            g[x - 1].append((y - 1, d))

        dis = [inf] * n
        dis[k - 1] = 0
        h = [(0, k - 1)]
        while h:
            dx, x = heappop(h)
            if dx > dis[x]:  # x 之前出堆过
                continue
            for y, d in g[x]:
                new_dis = dx + d
                if new_dis < dis[y]:
                    dis[y] = new_dis  # 更新 x 的邻居的最短路
                    heappush(h, (new_dis, y))
        mx = max(dis)
        return mx if mx < inf else -1


if __name__ == "__main__":
    sol = Solution()
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    print(sol.networkDelayTime(times, n, k))
    print(sol.networkDelayTime2(times, n, k))
    print(sol.networkDelayTime3(times, n, k))
