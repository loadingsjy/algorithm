#
# 498. 对角线遍历
# 给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。

# 示例 1：
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,4,7,5,3,6,8,9]
# 示例 2：
# 输入：mat = [[1,2],[3,4]]
# 输出：[1,2,3,4]


class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        def diagonal(mat, x1, y1, x2, y2, down=True):
            res = []
            if down:
                row, col = x1, y1
                while row <= x2:
                    res.append(mat[row][col])
                    row += 1
                    col -= 1
            else:
                row, col = x2, y2
                while row >= x1:
                    res.append(mat[row][col])
                    row -= 1
                    col += 1
            return res

        n, m = len(mat), len(mat[0])
        res = []
        x1, y1, x2, y2 = 0, 0, 0, 0
        down = False
        for _ in range(n + m - 1):
            res.extend(diagonal(mat, x1, y1, x2, y2, down))
            # x1, y1点一直向右走，走到最右再往下走
            if y1 != m - 1:
                y1 += 1
            else:
                x1 += 1
            # x2, y2点一直向下走，走到最下再往左走
            if x2 != n - 1:
                x2 += 1
            else:
                y2 += 1

            down = not down
        return res

    def findDiagonalOrder2(self, mat: list[list[int]]) -> list[int]:
        ans = []
        m, n = len(mat), len(mat[0])
        for i in range(m + n - 1):
            if i % 2:
                x = 0 if i < n else i - n + 1
                y = i if i < n else n - 1
                while x < m and y >= 0:
                    ans.append(mat[x][y])
                    x += 1
                    y -= 1
            else:
                x = i if i < m else m - 1
                y = 0 if i < m else i - m + 1
                while x >= 0 and y < n:
                    ans.append(mat[x][y])
                    x -= 1
                    y += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(s.findDiagonalOrder(mat))
    print(s.findDiagonalOrder2(mat))
    print()

    mat = [[1, 2], [3, 4]]
    print(s.findDiagonalOrder(mat))
    print(s.findDiagonalOrder2(mat))
