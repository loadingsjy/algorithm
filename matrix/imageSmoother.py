#
# * 661. 图片平滑器 - E
# 图像平滑器 是大小为 3 x 3 的过滤器，用于对图像的每个单元格平滑处理，平滑处理后单元格的值为该单元格的平均灰度。
# 每个单元格的  平均灰度 定义为：该单元格自身及其周围的 8 个单元格的平均值，结果需向下取整。（即，需要计算蓝色平滑器中 9 个单元格的平均值）。
# 如果一个单元格周围存在单元格缺失的情况，则计算平均灰度时不考虑缺失的单元格（即，需要计算红色平滑器中 4 个单元格的平均值）。

from itertools import product
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        """模拟"""
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tot, num = 0, 0
                for x in range(max(i - 1, 0), min(i + 2, m)):
                    for y in range(max(j - 1, 0), min(j + 2, n)):
                        tot += img[x][y]
                        num += 1
                ans[i][j] = tot // num
        return ans
    
    def imageSmoother2(self, img: List[List[int]]) -> List[List[int]]:
        """前缀和"""
        m, n = len(img), len(img[0])
        sum = [[0] * (n + 10) for _ in range(m + 10)]
        for i, j in product(range(1, m + 1), range(1, n + 1)):
            sum[i][j] = (
                sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + img[i - 1][j - 1]
            )
        ans = [[0] * n for _ in range(m)]
        for i, j in product(range(m), range(n)):
            a, b = max(0, i - 1), max(0, j - 1)
            c, d = min(m - 1, i + 1), min(n - 1, j + 1)
            cnt = (c - a + 1) * (d - b + 1)
            tot = sum[c + 1][d + 1] - sum[a][d + 1] - sum[c + 1][b] + sum[a][b]
            ans[i][j] = tot // cnt
        return ans


if __name__ == "__main__":
    sol = Solution()
    img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
    print(sol.imageSmoother(img))
    print(sol.imageSmoother2(img))