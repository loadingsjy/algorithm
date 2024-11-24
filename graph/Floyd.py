def Floyd(n, edges):
    """Floyd算法，得到图中任意两点之间的最短距离
    时间复杂度O(n^3)，空间复杂度O(n^2)，常数时间小，容易实现
    适用于任何图，不管有向无向、不管边权正负、但是不能有负环（保证最短路存在）"""

    distance = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        distance[i][i] = 0
    for u, v, w in edges:
        distance[u][v] = w

    # O(N^3)的过程
    # 枚举每个跳板(不关心跳点的枚举顺序) 看两点距离有没有变短
    # 注意，跳板要最先枚举！跳板要最先枚举！跳板要最先枚举！
    for bridge in range(n):  # 跳板
        for i in range(n):
            for j in range(n):
                # i -> .....bridge .... -> j
                # distance[i][j]能不能缩短
                # distance[i][j] = min ( distance[i][j] , distance[i][bridge] + distance[bridge][j])

                # if (
                #     distance[i][bridge] != float("inf")
                #     and distance[bridge][j] != float("inf")
                #     and distance[i][j] > distance[i][bridge] + distance[bridge][j]
                # ):
                if distance[i][j] > distance[i][bridge] + distance[bridge][j]:
                    distance[i][j] = distance[i][bridge] + distance[bridge][j]
