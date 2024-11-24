#
# * 474. 一和零 - M
# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
# 请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

# 示例 1：
# 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
# 示例 2：
# 输入：strs = ["10", "0", "1"], m = 1, n = 1
# 输出：2
# 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。

# 提示：
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] 仅由 '0' 和 '1' 组成
# 1 <= m, n <= 100

# * 问题转化为： 容量为n个‘1’和m个‘0’的背包 最多装多少个字符串
from functools import cache


def CountZerosAndOnes(s):
    temp = list(map(int, list(s)))
    cnt_1 = sum(temp)
    # cnt_0 = len(temp) - cnt_1
    return len(temp) - cnt_1, cnt_1


class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        """记忆化搜索"""

        @cache
        def dfs(i, z, o):
            """strs[0...i]自由选择，并且0的数量不超过z，1的数量不超过o，返回最多能选择多少个字符串"""
            if i == len(strs):
                return 0
            # 不使用当前的strs[i]字符串
            p1 = dfs(i + 1, z, o)
            cnt_0, cnt_1 = strs[i].count("0"), strs[i].count("1")
            # 使用当前的strs[i]字符串
            p2 = 0
            if cnt_0 <= z and cnt_1 <= o:
                p2 = 1 + dfs(i + 1, z - cnt_0, o - cnt_1)
            return max(p1, p2)

        return dfs(0, m, n)

    def findMaxForm2(self, strs: list[str], m: int, n: int) -> int:
        """空间压缩"""
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:  # 遍历所有字符串
            cnt_0, cnt_1 = s.count("0"), s.count("1")
            # 遍历所有容量为i个‘1’和j个‘0’的最多装多少个字符串
            for i in range(m, cnt_0 - 1, -1):
                for j in range(n, cnt_1 - 1, -1):
                    dp[i][j] = max(dp[i - cnt_0][j - cnt_1] + 1, dp[i][j])

        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    strs = ["101", "01", "111", "1100", "1010", "1011", "0111", "0011", "0001"]
    m, n = 8, 6
    print(sol.findMaxForm(strs, m, n))
    print(sol.findMaxForm2(strs, m, n))
