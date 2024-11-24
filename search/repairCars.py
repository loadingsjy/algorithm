#
# * 2594. 修车的最少时间 - M

# 给你一个整数数组 ranks ，表示一些机械工的 能力值 。ranksi 是第 i 位机械工的能力值。能力值为 r 的机械工可以在 r * n2 分钟内修好 n 辆车。
# 同时给你一个整数 cars ，表示总共需要修理的汽车数目。
# 请你返回修理所有汽车 最少 需要多少时间。
# 注意：所有机械工可以同时修理汽车。

# 示例 1：
# 输入：ranks = [4,2,3,1], cars = 10
# 输出：16
# 解释：
# - 第一位机械工修 2 辆车，需要 4 * 2 * 2 = 16 分钟。
# - 第二位机械工修 2 辆车，需要 2 * 2 * 2 = 8 分钟。
# - 第三位机械工修 2 辆车，需要 3 * 2 * 2 = 12 分钟。
# - 第四位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
# 16 分钟是修理完所有车需要的最少时间。
# 示例 2：
# 输入：ranks = [5,1,8], cars = 6
# 输出：16
# 解释：
# - 第一位机械工修 1 辆车，需要 5 * 1 * 1 = 5 分钟。
# - 第二位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
# - 第三位机械工修 1 辆车，需要 8 * 1 * 1 = 8 分钟。
# 16 分钟时修理完所有车需要的最少时间。

# 提示：
# 1 <= ranks.length <= 105
# 1 <= ranks[i] <= 100
# 1 <= cars <= 106


import math
from bisect import bisect_left
from collections import Counter


class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        """二分答案，自己写的"""

        # def check(time):
        #     """返回time时间内最多能修多少俩车"""
        #     total = 0
        #     for r in ranks:
        #         total += int(math.sqrt(time / r))
        #     return total

        l, r = 0, min(ranks) * cars * cars  # 最快0分钟修完车，最慢min*n*n分钟修完车
        while l <= r:
            mid = (l + r) // 2
            if sum([int(math.sqrt(mid / r)) for r in ranks]) >= cars:
                r = mid - 1
            else:
                l = mid + 1
        return l  # 最小的满足要求的值

    def repairCars2(self, ranks: list[int], cars: int) -> int:
        """库函数写法"""
        s = lambda t: sum(math.isqrt(t // r) for r in ranks)
        return bisect_left(range(min(ranks) * cars * cars), cars, key=s)

    def repairCars3(self, ranks: list[int], cars: int) -> int:
        """优化：观测数据
        能力值相同的人，在 t 分钟内修好的车的个数是一样的。
        根据数据范围，ranks 中至多有 100 个不同的数字，我们可以统计 ranks 中每个数字的出现次数，这样每次二分至多循环 100 次。
        此外，如果循环中发现 s≥cars，可以提前退出循环。"""
        cnt = Counter(ranks)
        left = 0
        right = min(cnt) * cars * cars
        while left + 1 < right:
            mid = (left + right) // 2
            if sum(math.isqrt(mid // r) * c for r, c in cnt.items()) >= cars:
                right = mid
            else:
                left = mid
        return right

    def repairCars4(self, ranks: list[int], cars: int) -> int:
        """优化后库函数写法"""
        cnt = Counter(ranks)
        s = lambda t: sum(math.isqrt(t // r) * c for r, c in cnt.items())
        return bisect_left(range(min(cnt) * cars * cars), cars, key=s)


if __name__ == "__main__":
    sol = Solution()
    ranks = [4, 2, 3, 1]
    cars = 10
    print(sol.repairCars(ranks, cars))
    print(sol.repairCars2(ranks, cars))
    print(sol.repairCars3(ranks, cars))
    print(sol.repairCars4(ranks, cars))
