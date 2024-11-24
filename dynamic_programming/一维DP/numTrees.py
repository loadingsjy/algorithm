# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)  # dp[i] 表示有 i 个节点的二叉搜索树的种数
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):  # 枚举根节点/左数节点个数
                # 左子树的节点数为 j-1，右子树的节点数为 i-j
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(3))  # Output: 5
    print(s.numTrees(4))  # Output: 14
