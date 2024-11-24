#
# * 1168. 水资源分配优化 - H
# 村里面一共有 n 栋房子。我们希望通过建造水井和铺设管道来为所有房子供水。
# 对于每个房子 i，我们有两种可选的供水方案：一种是直接在房子内建造水井，成本为 wells[i - 1] （注意 -1 ，因为 索引从0开始 ）；
# 另一种是从另一口井铺设管道引水，数组 pipes 给出了在房子间铺设管道的成本，
# 其中每个 pipes[j] = [house1j, house2j, costj] 代表用管道将 house1j 和 house2j连接在一起的成本。连接是双向的。
# 请返回 为所有房子都供水的最低总成本 。

# 示例 1：
# 输入：n = 2, wells = [1,1], pipes = [[1,2,1]]
# 输出：2
# 解释：我们可以用以下三种方法中的一种来提供低成本的水:
# 选项1:
# 在1号房子里面建一口井，成本为1
# 在房子2内建造井，成本为1
# 总成本是2。
# 选项2:
# 在1号房子里面建一口井，成本为1
# -花费1连接房子2和房子1。
# 总成本是2。
# 选项3:
# 在房子2内建造井，成本为1
# -花费1连接房子1和房子2。
# 总成本是2。
# 注意，我们可以用cost 1或cost 2连接房子1和房子2，但我们总是选择最便宜的选项。

# 提示：
# 2 <= n <= 104
# wells.length == n
# 0 <= wells[i] <= 105
# 1 <= pipes.length <= 104
# pipes[j].length == 3
# 1 <= house1j, house2j <= n
# 0 <= costj <= 105
# house1j != house2j


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


class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):
        """引入超级水源，连接每个村庄，并将边的权重设置为直接在房子内建造水井的成本，
        将问题转化为求最小生成树"""

        def kruskal(n, edges):
            """kruskal 最小生成树算法"""
            uf = UF(n)
            edges.sort(key=lambda x: x[2])
            nodes_count = 1
            ans = 0
            for u, v, w in edges:
                if uf.union(u, v):  # 两个点在一个集合不能合并，否则会形成环
                    ans += w
                    nodes_count += 1
            return ans if nodes_count == n else "orz"

        pipes.extend([[0, i + 1, well] for i, well in enumerate(wells)])
        return kruskal(n + 1, pipes)
