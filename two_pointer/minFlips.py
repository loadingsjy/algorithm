#
# * 3239. 最少翻转次数使二进制矩阵回文 I - M
# 给你一个 m x n 的二进制矩阵 grid 。
# 如果矩阵中一行或者一列从前往后与从后往前读是一样的，那么我们称这一行或者这一列是 回文 的。
# 你可以将 grid 中任意格子的值 翻转 ，也就是将格子里的值从 0 变成 1 ，或者从 1 变成 0 。
# 请你返回 最少 翻转次数，使得矩阵 要么 所有行是 回文的 ，要么所有列是 回文的 。

from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        def fun(array):
            res = 0
            i, j = 0, len(array) - 1
            while i < j:
                if array[i] != array[j]:
                    res += 1
                i += 1
                j -= 1
            return res

        ans1 = 0
        for row_data in grid:
            ans1 += fun(row_data)
        ans2 = 0
        for col_data in zip(*grid):
            ans2 += fun(col_data)
        return min(ans1, ans2)

    def minFlips2(self, grid: List[List[int]]) -> int:
        diff_row = 0
        for row in grid:
            for j in range(len(row) // 2):
                if row[j] != row[-1 - j]:
                    diff_row += 1

        diff_col = 0
        for col in zip(*grid):
            for i in range(len(grid) // 2):
                if col[i] != col[-1 - i]:
                    diff_col += 1

        return min(diff_row, diff_col)


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
    print(sol.minFlips(grid))
    print(sol.minFlips2(grid))
