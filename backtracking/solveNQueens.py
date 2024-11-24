# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        col = [0] * n  # col[i]代表第i行第col[i]列放皇后

        # def vaild(r, c):
        #     for R in range(r):
        #         C = col[R]
        #         if r + c == R + C or r - c == R - C:
        #             return False
        #     return True

        def dfs(r, s) -> None:
            if r == n:
                ans.append(["." * c + "Q" + "." * (n - 1 - c) for c in col])
                return
            for c in s:
                if all(r + c != R + col[R] and r - c != R - col[R] for R in range(r)):
                    col[r] = c
                    dfs(r + 1, s - {c})

        dfs(0, set(range(n)))
        return ans

    def solveNQueens_improved(self, n: int) -> list[list[str]]:
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


if __name__ == "__main__":
    s = Solution()
    n = 4
    print(s.solveNQueens(n))
    print(s.solveNQueens_improved(n))
