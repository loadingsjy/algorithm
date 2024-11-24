#
# * 2132. 用邮票贴满网格图 - H

# 给你一个 m x n 的二进制矩阵 grid ，每个格子要么为 0 （空）要么为 1 （被占据）。
# 给你邮票的尺寸为 stampHeight x stampWidth 。我们想将邮票贴进二进制矩阵中，且满足以下 限制 和 要求 ：

# 1.覆盖所有 空 格子。
# 2.不覆盖任何 被占据 的格子。
# 3.我们可以放入任意数目的邮票。
# 4.邮票可以相互有 重叠 部分。
# 5.邮票不允许 旋转 。
# 6.邮票必须完全在矩阵 内 。
# 7.如果在满足上述要求的前提下，可以放入邮票，请返回 true ，否则返回 false 。

# 提示：
# m == grid.length
# n == grid[r].length
# 1 <= m, n <= 105
# 1 <= m * n <= 2 * 105
# grid[r][c] 要么是 0 ，要么是 1 。
# 1 <= stampHeight, stampWidth <= 105


class Solution:
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        """
        思路:
        1.由于邮票可以互相重叠，贪心地想，能放邮票就放邮票。
        2.遍历所有能放邮票的位置去放邮票。注意邮票不能覆盖被占据的格子，也不能出界。
        3.放邮票的同时，记录每个空格子被多少张邮票覆盖。如果存在一个空格子没被邮票覆盖，则返回 false，否则返回 true。

        细节:
        1.怎么快速判断一个矩形区域可以放邮票？求出 grid 的二维前缀和，从而 O(1) 地求出任意矩形区域的元素和。
        如果一个矩形区域的元素和等于 0，就表示该矩形区域的所有格子都是 0。
        2.假设用一个二维计数矩阵 cnt 记录每个空格子被多少张邮票覆盖，那么放邮票时，就需要把 cnt 的一个矩形区域都加一。
        怎么快速实现？可以用二维差分矩阵 d 来代替 cnt。矩形区域都加一的操作，转变成 O(1) 地对 d 中四个位置的更新操作。
        3.最后从二维差分矩阵 d 还原出二维计数矩阵 cnt。类似对一维差分数组求前缀和得到原数组，我们需要对二维差分矩阵求二维前缀和。
        遍历 cnt，如果存在一个空格子的计数值为 0，就表明该空格子没有被邮票覆盖，返回 false，否则返回 true。
        代码实现时，可以直接在 d 数组上原地计算出 cnt。
        """
        m, n = len(grid), len(grid[0])

        # 1. 计算 grid 的二维前缀和
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + v

        # 2. 计算二维差分
        # 为方便第 3 步的计算，在 d 数组的最上面和最左边各加了一行（列），所以下标要 +1
        d = [[0] * (n + 2) for _ in range(m + 2)]
        for i2 in range(stampHeight, m + 1):
            for j2 in range(stampWidth, n + 1):
                i1 = i2 - stampHeight + 1
                j1 = j2 - stampWidth + 1
                if s[i2][j2] - s[i2][j1 - 1] - s[i1 - 1][j2] + s[i1 - 1][j1 - 1] == 0:
                    d[i1][j1] += 1
                    d[i1][j2 + 1] -= 1
                    d[i2 + 1][j1] -= 1
                    d[i2 + 1][j2 + 1] += 1

        # 3. 还原二维差分矩阵对应的计数矩阵（原地计算）
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                d[i + 1][j + 1] += d[i + 1][j] + d[i][j + 1] - d[i][j]
                if v == 0 and d[i + 1][j + 1] == 0:
                    return False
        return True

    def possibleToStamp(self, grid, stampHeight, stampWidth):
        m, n = len(grid), len(grid[0])
        psum = [[0] * (n + 2) for _ in range(m + 2)]
        diff = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                psum[i][j] = (
                    psum[i - 1][j]
                    + psum[i][j - 1]
                    - psum[i - 1][j - 1]
                    + grid[i - 1][j - 1]
                )

        for i in range(1, m + 2 - stampHeight):
            for j in range(1, n + 2 - stampWidth):
                x = i + stampHeight - 1
                y = j + stampWidth - 1
                if (
                    psum[x][y] - psum[x][j - 1] - psum[i - 1][y] + psum[i - 1][j - 1]
                    == 0
                ):
                    diff[i][j] += 1
                    diff[i][y + 1] -= 1
                    diff[x + 1][j] -= 1
                    diff[x + 1][y + 1] += 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
                if diff[i][j] == 0 and grid[i - 1][j - 1] == 0:
                    return False
        return True
