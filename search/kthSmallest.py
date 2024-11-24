#
# * 378. 有序矩阵中第 K 小的元素 - M
# 给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。
# 你必须找到一个内存复杂度优于 O(n2) 的解决方案。

# 示例 1：
# 输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# 输出：13
# 解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13
# 示例 2：
# 输入：matrix = [[-5]], k = 1
# 输出：-5

# 提示：
# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 300
# -109 <= matrix[i][j] <= 109
# 题目数据 保证 matrix 中的所有行和列都按 非递减顺序 排列
# 1 <= k <= n2

# 进阶：
# 你能否用一个恒定的内存(即 O(1) 内存复杂度)来解决这个问题?
# 你能在 O(n) 的时间复杂度下解决这个问题吗?这个方法对于面试来说可能太超前了，但是你会发现阅读这篇文章（ this paper ）很有趣。
import heapq


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        """时间复杂度：O(nlog(r−l))，二分查找进行次数为 O(log(r−l))，每次操作时间复杂度为 O(n)。空间复杂度：O(1)。"""
        n = len(matrix)

        def count(num):
            ans = 0
            row, col = 0, n - 1
            while row < n and col >= 0:
                if matrix[row][col] <= num:
                    ans += col + 1
                    row += 1
                else:
                    col -= 1
            return ans

        # l = min([num for num in min(matrix)])
        # r = max([num for num in max(matrix)])
        l = matrix[0][0]
        r = matrix[-1][-1]
        while l <= r:
            mid = (l + r) // 2
            if count(mid) >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l

    def kthSmallest2(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)  # 注：题目中这个矩阵是n*n的，所以长宽都是n

        pq = [(matrix[i][0], i, 0) for i in range(n)]  # 取出第一列候选人
        # matrix[i][0]是具体的值，后面的(i,0)是在记录候选人在矩阵中的位置，方便每次右移添加下一个候选人

        heapq.heapify(pq)  # 变成一个heap

        for i in range(k - 1):  # 一共弹k次：这里k-1次，return的时候1次
            num, x, y = heapq.heappop(pq)  # 弹出候选人里最小一个
            if y != n - 1:  # 如果这一行还没被弹完
                # 加入这一行的下一个候选人
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))

        return heapq.heappop(pq)[0]


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(sol.kthSmallest(matrix, k))
    print(sol.kthSmallest2(matrix, k))
