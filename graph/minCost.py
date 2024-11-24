#
# * 1928. 规定时间内到达终点的最小花费 - H
# 一个国家有 n 个城市，城市编号为 0 到 n - 1 ，题目保证 所有城市 都由双向道路 连接在一起 。道路由二维整数数组 edges 表示，其中 edges[i] = [xi, yi, timei] 表示城市 xi 和 yi 之间有一条双向道路，耗费时间为 timei 分钟。两个城市之间可能会有多条耗费时间不同的道路，但是不会有道路两头连接着同一座城市。
# 每次经过一个城市时，你需要付通行费。通行费用一个长度为 n 且下标从 0 开始的整数数组 passingFees 表示，其中 passingFees[j] 是你经过城市 j 需要支付的费用。
# 一开始，你在城市 0 ，你想要在 maxTime 分钟以内 （包含 maxTime 分钟）到达城市 n - 1 。旅行的 费用 为你经过的所有城市 通行费之和 （包括 起点和终点城市的通行费）。
# 给你 maxTime，edges 和 passingFees ，请你返回完成旅行的 最小费用 ，如果无法在 maxTime 分钟以内完成旅行，请你返回 -1 。
# 示例 1：
# 输入：maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
# 输出：11
# 解释：最优路径为 0 -> 1 -> 2 -> 5 ，总共需要耗费 30 分钟，需要支付 11 的通行费。
# 提示：
# 1 <= maxTime <= 1000
# n == passingFees.length
# 2 <= n <= 1000
# n - 1 <= edges.length <= 1000
# 0 <= xi, yi <= n - 1
# 1 <= timei <= 1000
# 1 <= passingFees[j] <= 1000
# 图中两个节点之间可能有多条路径。
# 图中不含有自环。
import heapq


class Solution:
    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]):
        """堆优化 Dijkstra + DP"""
        n = len(passingFees)
        g = [[] for _ in range(n)]  # 用邻接表存储图
        for u, v, time in edges:
            g[u].append((v, time))  # 添加边 u -> v
            g[v].append((u, time))  # 添加边 v -> u

        dist = [[float("inf")] * (maxTime + 1) for _ in range(n)]  # 初始化距离数组
        dist[0][0] = passingFees[0]  # 起点费用
        pq = [(dist[0][0], 0, 0)]  # (最小费用, 当前节点, 累计时间)

        while pq:
            # 从源点到当前的的花费、到达的city、目前花费的时间
            cost, city, curTime = heapq.heappop(pq)
            for neighbor, edgeTime in g[city]:
                newCost = cost + passingFees[neighbor]  # 通行费
                newTime = curTime + edgeTime  # 总时间
                if newTime <= maxTime and newCost < dist[neighbor][newTime]:
                    dist[neighbor][newTime] = newCost
                    heapq.heappush(pq, (newCost, neighbor, newTime))

        res = min(dist[-1])
        return res if res != float("inf") else -1

    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]):
        """BellmanFord算法"""
        # Bellman Ford
        n = len(passingFees)
        INF = float("inf")
        # dp[t][u]表示花费t时间到点u的最小花费
        dp = [[INF] * (n) for _ in range(maxTime + 1)]
        dp[0][0] = passingFees[0]  # 边界值

        for t in range(1, maxTime + 1):  # 第一维枚举时间
            for u, v, w in edges:  # 第二维遍历图
                if t >= w:
                    dp[t][v] = min(dp[t][v], dp[t - w][u] + passingFees[v])
                    dp[t][u] = min(dp[t][u], dp[t - w][v] + passingFees[u])

        # 寻找最小值
        ans = min(dp[i][n - 1] for i in range(1, maxTime + 1))
        return -1 if ans == INF else ans

    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]):
        """动态规划"""
        n = len(passingFees)
        f = [[float("inf")] * n for _ in range(maxTime + 1)]
        f[0][0] = passingFees[0]
        for t in range(1, maxTime + 1):
            for i, j, cost in edges:
                if cost <= t:
                    f[t][i] = min(f[t][i], f[t - cost][j] + passingFees[i])
                    f[t][j] = min(f[t][j], f[t - cost][i] + passingFees[j])

        ans = min(f[t][n - 1] for t in range(1, maxTime + 1))
        return -1 if ans == float("inf") else ans
