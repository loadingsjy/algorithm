# 给你一个满足下述两条属性的 m x n 整数矩阵：
# 每行中的整数从左到右按非严格递增顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """一次二分查找，看做把二维矩阵展开为一维数组，时间复杂度O(log(nm))"""
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = n * m - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid // m][mid % m] == target:
                return True
            if matrix[mid // m][mid % m] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """两次次二分查找，先找到行，再找到列，时间复杂度O(logn+logm)=log(nm)"""
        n = len(matrix)
        m = len(matrix[0])

        low = 0
        high = n - 1
        # 先确定行号x
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        if high == -1:
            return False
        x = high

        low = 0
        high = m - 1
        # 从该行二分查找
        while low <= high:
            mid = (low + high) // 2
            if matrix[x][mid] == target:
                return True
            elif matrix[x][mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False
