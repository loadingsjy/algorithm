# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# * 每行的元素从左到右升序排列。
# * 每列的元素从上到下升序排列。
from bisect import bisect


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """思路：从左上角开始，target每次都和当前的左上角元素比较，如果比它大，则当前行的数字都不可能成为答案；
        如果比它小，则当前列的数字都不可成为答案（从右下角开始也可以）
        时间复杂度O(n+m)"""

        n = len(matrix)
        m = len(matrix[0])

        row = 0
        col = m - 1
        while row < n and col >= 0:
            cur = matrix[row][col]
            if target == cur:
                return True
            elif target > cur:
                row += 1
            else:
                col -= 1
        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """思路：分别对每一行都进行二分查找，时间复杂度：O(mlogn)"""
        for row in matrix:
            idx = bisect.bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True
        return False
