# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 你可以按 任何顺序 返回答案。

# 示例 1：
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# 示例 2：
# 输入：n = 1, k = 1
# 输出：[[1]]


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        n_lst = list(range(1, n + 1))
        ans = []
        res = []

        def dfs(i):
            # 剪枝：res当前的长度加上剩下可选的长度<k，那么不能凑出k长度的组合
            if len(res) + n - i + 1 < k:
                return
            if i == n and k > len(res):
                return
            if k == len(res):
                ans.append(res[:])
                return
            # 不选
            dfs(i + 1)
            # 选
            res.append(n_lst[i])
            dfs(i + 1)
            res.pop()

        dfs(0)
        return ans
