#
# * 3240. 最少翻转次数使二进制矩阵回文 II - M
# 给你一个 m x n 的二进制矩阵 grid 。
# 如果矩阵中一行或者一列从前往后与从后往前读是一样的，那么我们称这一行或者这一列是 回文 的。
# 你可以将 grid 中任意格子的值 翻转 ，也就是将格子里的值从 0 变成 1 ，或者从 1 变成 0 。
# 请你返回 最少 翻转次数，使得矩阵中 所有 行和列都是 回文的 ，且矩阵中 1 的数目可以被 4 整除

from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        """由于所有行和列都必须是回文的，所以要满足 a[i][j]=a[i][n−1−j]=a[m−1−i][j]=a[m−1−i][n−1−j]
        也就是这四个数要么都是 0，要么都是 1。其中 0≤i<⌊m/2⌋, 0≤j<⌊n/2⌋。
        设cnt1=a[i][j]+a[i][n−1−j]+a[m−1−i][j]+a[m−1−i][n−1−j]
        把这四个数都变成 0 需要翻转 cnt1次，都变成 1 需要翻转 4−cnt1次。两种情况取最小值，把min(cnt1​,4−cnt1​)加入答案。
        
        通过上面的操作，矩阵中 1 的数目一定可以被 4 整除
        接下來在判斷行和列为奇数的时候，中间行和列如何变换成回文的，并且1的数量能被4整除。"""
        
        n, m = len(grid), len(grid[0])
        ans = 0
        for x in range(n // 2):
            for y in range(m // 2):
                ones = 0
                ones = (
                    grid[x][y]
                    + grid[n - 1 - x][y]
                    + grid[n - 1 - x][m - 1 - y]
                    + grid[x][m - 1 - y]
                )
                ans += min(ones, 4 - ones)

        if n & 1 and m & 1 and grid[n // 2][m // 2]:
            ans += 1

        diff = 0
        same_ones = 0  # 正中间行和正中间列的镜像位置的1的个数
        # 统计正中间的那一行
        if n & 1:
            mid = n // 2
            for i in range(m // 2):
                if grid[mid][i] != grid[mid][m - 1 - i]:
                    diff += 1
                else:
                    same_ones += grid[mid][i] * 2

        # 统计正中间的那一列
        if m & 1:
            mid = m // 2
            for i in range(n // 2):
                if grid[i][mid] != grid[n - 1 - i][mid]:
                    diff += 1
                else:
                    same_ones += grid[i][mid] * 2

        return ans + (diff if diff else same_ones % 4)


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(sol.minFlips(grid))
