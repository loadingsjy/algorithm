#
# * 2421. 好路径的数目 - H
# 给你一棵 n 个节点的树（连通无向无环的图），节点编号从 0 到 n - 1 且恰好有 n - 1 条边。
# 给你一个长度为 n 下标从 0 开始的整数数组 vals ，分别表示每个节点的值。同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 无向 边。
# 一条 好路径 需要满足以下条件：
# 开始节点和结束节点的值 相同 。
# 开始节点和结束节点中间的所有节点值都 小于等于 开始节点的值（也就是说开始节点的值应该是路径上所有节点的最大值）。
# 请你返回不同好路径的数目。
# 注意，一条路径和它反向的路径算作 同一 路径。比方说， 0 -> 1 与 1 -> 0 视为同一条路径。单个节点也视为一条合法路径。

# 示例 1 :
# 输入：vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
# 输出：6
# 解释：总共有 5 条单个节点的好路径。
# 还有 1 条好路径：1 -> 0 -> 2 -> 4 。
# （反方向的路径 4 -> 2 -> 0 -> 1 视为跟 1 -> 0 -> 2 -> 4 一样的路径）
# 注意 0 -> 2 -> 3 不是一条好路径，因为 vals[2] > vals[0] 。

# 提示：
# n == vals.length
# 1 <= n <= 3 * 104
# 0 <= vals[i] <= 105
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges 表示一棵合法的树。


class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        """并查集，根据集团最大值进行合并"""
        n = len(vals)
        father = [i for i in range(n)]
        maxCount = [1] * n

        def find(i):
            if i != father[i]:
                father[i] = find(father[i])
            return father[i]

        def union(x, y):
            fx = find(x)
            fy = find(y)
            path = 0
            if vals[fx] > vals[fy]:
                father[fy] = fx
            elif vals[fx] < vals[fy]:
                father[fx] = fy
            else:
                father[fy] = fx
                path = maxCount[fx] * maxCount[fy]
                maxCount[fx] += maxCount[fy]
            return path

        # 必须按照每条边上两个节点的最大值排序处理每条边，这样保证最大值是有序的
        edges.sort(key=lambda e: max(vals[e[0]], vals[e[1]]))
        ans = n
        for edge in edges:
            ans += union(edge[0], edge[1])
        return ans


if __name__ == "__main__":
    sol = Solution()
    vals = [1, 3, 2, 1, 3]
    edges = [[0, 1], [0, 2], [2, 3], [2, 4]]
    print(sol.numberOfGoodPaths(vals, edges))
