#
# * 3249. 统计好节点的数目
# 现有一棵 无向 树，树中包含 n 个节点，按从 0 到 n - 1 标记。树的根节点是节点 0 ,
# 给你一个长度为 n - 1 的二维整数数组 edges，其中 edges[i] = [ai, bi] 表示树中节点 ai 与节点 bi 之间存在一条边。
# 如果一个节点的所有子节点为根的树包含的节点数相同，则认为该节点是一个 好节点。
# 返回给定树中 好节点 的数量。
# 子树 指的是一个节点以及它所有后代节点构成的一棵树。

from typing import List


class Solution:

    def countGoodNodes(self, edges: List[List[int]]) -> int:
        """
        建树，然后从根节点 0 开始 DFS 这棵树。DFS 返回子树大小。
        对于节点 x，如果其是叶子节点，或者其所有儿子子树大小都一样，那么答案加一。
        """
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = 0

        def dfs(x: int, fa: int) -> int:
            size, pre, ok = 1, 0, True
            for y in g[x]:
                if y == fa:
                    continue  # 不能递归到父节点
                child_size = dfs(y, x)
                if pre == 0:
                    pre = child_size  # 记录第一个儿子子树的大小
                elif child_size != pre:  # 存在大小不一样的儿子子树
                    ok = False  # 注意不能 break，其他子树 y 仍然要递归
                size += child_size
            nonlocal ans
            ans += ok
            return size

        dfs(0, -1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    edges = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [1, 6], [2, 7], [3, 8]]
    print(sol.countGoodNodes(edges))
