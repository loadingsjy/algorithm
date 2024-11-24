# * 2352. 相等行列对
# 给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。
# 如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。


from collections import Counter, defaultdict
from typing import List


class Solution:

    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        records = defaultdict(int)
        for i in range(n):
            records[tuple(grid[i])] += 1
        ans = 0
        for i in range(n):
            if (t := tuple([row[i] for row in grid])) in records:
                ans += records[t]
        return ans

    def equalPairs(self, grid: List[List[int]]) -> int:
        """灵神写法 用哈希表统计每行出现的次数，然后遍历列，累加哈希表中列出现的次数。"""
        cnt = Counter(tuple(row) for row in grid)
        return sum(cnt[col] for col in zip(*grid))


if __name__ == "__main__":
    sol = Solution()
    grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    print(sol.equalPairs(grid))
