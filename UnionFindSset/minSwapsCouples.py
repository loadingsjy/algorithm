#
# * 765. 情侣牵手 - H
# n 对情侣坐在连续排列的 2n 个座位上，想要牵到对方的手。
# 人和座位由一个整数数组 row 表示，其中 row[i] 是坐在第 i 个座位上的人的 ID。
# 情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2n-2, 2n-1)。
# 返回 最少交换座位的次数，以便每对情侣可以并肩坐在一起。 每次交换可选择任意两人，让他们站起来交换座位。


# 示例 1:
# 输入: row = [0,2,1,3]
# 输出: 1
# 解释: 只需要交换row[1]和row[2]的位置即可。
# 示例 2:
# 输入: row = [3,2,0,1]
# 输出: 0
# 解释: 无需交换座位，所有的情侣都已经可以手牵手了。

# 提示:
# 2n == row.length
# 2 <= n <= 30
# n 是偶数
# 0 <= row[i] < 2n
# row 中所有元素均无重复


class UF:
    """并查集"""

    def __init__(self, n):
        self.father = [i for i in range(n)]
        self.sets = n  # 集合数量

    def find(self, i):
        if i != self.father[i]:
            self.father[i] = self.find(self.father[i])
        return self.father[i]

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.father[fx] = fy
            self.sets -= 1


class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        """并查集方法：至少交换的次数 = 所有情侣的对数 - 并查集里连通分量的个数"""
        n = len(row)
        uf = UF(n // 2)
        for i in range(0, n, 2):
            uf.union(row[i] // 2, row[i + 1] // 2)
        return n // 2 - uf.sets

    def minSwapsCouples2(self, row: list[int]) -> int:
        """
        贪心策略：我们遍历每个偶数位置 2∗i ，把它的对象安排到它右边的奇数位置 2∗i+1。
        如果一个人的编号为 x，那么他的情侣的编号为 x ^ 1
        """
        N = len(row)
        res = 0
        for i in range(0, N - 1, 2):
            if row[i] == row[i + 1] ^ 1:
                continue
            for j in range(i + 1, N):
                if row[i] == row[j] ^ 1:
                    row[i + 1], row[j] = row[j], row[i + 1]
            res += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    row = [0, 2, 1, 3]
    print(sol.minSwapsCouples(row))
    print(sol.minSwapsCouples2(row))
