from bisect import bisect_left
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        每行进行二分查找
        时间复杂度：二分查找一行的时间复杂度为logm，需要遍历n行，所以总时间复杂度是O(nlogm)。
        空间复杂度：O(1)。
        """
        n, m = len(grid), len(grid[0])
        ans = 0
        for i, row in enumerate(grid):
            if row[0] < 0:
                ans += m * (n - i)
                break
            # print(bisect_right(row[::-1], 0))
            ans += bisect_left(row[::-1], 0)
            # print(ans)
        return ans

    def countNegatives2(self, grid: List[List[int]]) -> int:
        """
        倒序遍历: 考虑我们已经算出第 i 行的从前往后第一个负数的位置 posi​，
        那么第 i+1 行的时候，posi+1的位置肯定是位于 [0,posi] 中，所以对于第 i+1 行我们倒着从 posi​循环找 posi+1​即可，这个循环起始变量是一直在递减的。
        时间复杂度：考虑每次循环变量的起始位置是单调不降的，所以起始位置最多移动 m 次，时间复杂度 O(n+m)。
        空间复杂度：O(1)。
        """
        n, m = len(grid), len(grid[0])
        ans = 0
        temp = m - 1
        for i in range(n):
            j = temp
            while j >= 0 and grid[i][j] < 0:
                j -= 1
            ans += m - 1 - j
            temp = j
        return ans


if __name__ == "__main__":
    sol = Solution()
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(sol.countNegatives(grid))
