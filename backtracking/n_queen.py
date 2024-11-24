#
# * 51. N 皇后 - H
# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 示例1：
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 示例 2：
# 输入：n = 1
# 输出：[["Q"]]


# 解决N皇后问题的时间复杂度是O(n!)，好的方法可以大量剪枝，大量优化常数时间

# 用数组表示路径的方法（经典、常数时间慢，不推荐）
# * 1.记录之前每一行的皇后放在了什么列
# * 2.来到第i行的时候，可以根据0..row-1行皇后的位置，判断能放哪些列
# * 3.把能放的列都尝试一遍，每次尝试修改路径数组表示当前的决策，后续返回的答案都累加返回


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        m = n * 2 - 1
        ans = []
        col = [0] * n
        on_path, diag1, diag2 = [False] * n, [False] * m, [False] * m

        def dfs(r: int) -> None:
            if r == n:
                ans.append(["." * c + "Q" + "." * (n - 1 - c) for c in col])
                return
            for c, on in enumerate(on_path):
                if not on and not diag1[r + c] and not diag2[r - c]:
                    col[r] = c
                    on_path[c] = diag1[r + c] = diag2[r - c] = True
                    dfs(r + 1)
                    on_path[c] = diag1[r + c] = diag2[r - c] = False  # 恢复现场

        dfs(0)
        return ans

    def solveNQueens2(self, n: int) -> list[list[str]]:
        ans = []
        col = [0] * n  # col[i]代表第i行第col[i]列放皇后

        def vaild(r, c):
            for R in range(r):
                C = col[R]
                if r + c == R + C or r - c == R - C:
                    return False
            return True

        def dfs(r, s) -> None:  # 从r行开始摆皇后，s是可选择的列号集合
            if r == n:
                ans.append(["." * c + "Q" + "." * (n - 1 - c) for c in col])
                return
            for c in s:
                # if all(r + c != R + col[R] and r - c != R - col[R] for R in range(r)):
                if vaild(r, c):
                    col[r] = c
                    dfs(r + 1, s - {c})

        dfs(0, set(range(n)))
        return ans

    def solveNQueens3(self, n: int) -> list[list[str]]:
        """返回方法数"""
        if n < 1:
            return 0
        path = [0] * n

        # 只判断0到row-1行是否有冲突
        # 返回row行皇后放在了col列，是否有效
        def check(row, col):
            for i in range(row):
                # 当前皇后的列和之前的列不能一样，且不能共斜线
                if path[i] == col or abs(col - path[i]) == abs(row - i):
                    return False
            return True

        # n皇后问题（默认每行摆一个皇后），当前来到第row行，path数组：0 - row-1 前面已经选择的列号，填完后面皇后的方法数
        def dfs(row):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if check(row, col):
                    path[row] = col
                    count += dfs(row + 1)
            return count

        return dfs(0)


if __name__ == "__main__":
    s = Solution()
    n = 4
    # print(s.solveNQueens(n))
    # print(s.solveNQueens2(n))
    print(s.solveNQueens3(n))
