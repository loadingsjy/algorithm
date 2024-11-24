#
# 668. 乘法表中第k小的数 - H

# 几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第 k 小的数字吗？
# 乘法表是大小为 m x n 的一个整数矩阵，其中 mat[i][j] == i * j（下标从 1 开始）。
# 给你三个整数 m、n 和 k，请你在大小为 m x n 的乘法表中，找出并返回第 k 小的数字。
from bisect import bisect_left


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """我们考虑如何进行「二分答案」: 假设当前我们二分到的值是 mid，对于乘法表中的每行和每列均是单调递增，
        我们可以通过累加统计 每行/每列 中比 mid 小的数，记作 a，累加统计 每行/每列 中等于 mid 的数，记作 b，
        那么 cnt=a+b 即是整个乘法表中小于等于 mid 的数的个数，再通过 cnt 和 k 的大小关系来指导左右指针的变化。

        具体的，假设我们通过枚举行来统计 a 和 b，当前枚举到的行号为 i（行号从 1 开始），该行的最大数为 i×m：
        1.若 i×m<mid，整行都是小于 mid 的数，直接在 a 基础上累加 m；
        2.若 i×m>=mid，根据 mid 是否存在于该行进行分情况讨论：
            1)mid 能够被 i 整除，说明 mid 存在于该行，那么比 mid 小的数的个数为i/mid​−1，将其累加到 a，同时对 b 进行加一；
            2)mid 不能够被 i 整除，说明 mid 不存在于该行，那么比 mid 小的数的个数为i/mid​，将其累加到 a。
        """

        # def count(num):
        #     """统计乘法表中小等于num的数的个数"""
        #     ans = 0
        #     for i in range(1, n + 1):
        #         ans += m if i * m <= num else num // i
        #     return ans

        l = 1
        r = m * n
        while l <= r:
            mid = (l + r) // 2
            if sum([m if i * m <= mid else mid // i for i in range(1, n + 1)]) >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """库函数写法"""
        return bisect_left(
            range(m * n),
            k,
            key=lambda x: x // n * n + sum(x // i for i in range(x // n + 1, m + 1)),
        )
