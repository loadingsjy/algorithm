# 有n个咖啡机，每个咖啡机的生产一杯咖啡的时间为arrs[i]，一共有n个人需要喝咖啡，每个人喝一杯咖啡的时间为0。
# 每个洗咖啡机的洗咖啡的时间为a，每个咖啡杯自然挥发的时间为b。
# 求n个人每人喝完一杯咖啡和洗完所有咖啡杯的最少时间？

import heapq
import numpy as np


class machine(object):
    def __init__(self, a, b):
        self.timePoint = a
        self.workTime = b

    def __lt__(self, other):
        return (self.timePoint + self.workTime) < (other.timePoint + other.workTime)


def minTime(arrs, n, a, b):
    heap = []
    for i in range(len(arrs)):
        heap.append(machine(0, arrs[i]))
    heapq.heapify(heap)
    drinks = [0] * n
    for i in range(n):
        cur = heapq.heappop(heap)
        cur.timePoint += cur.workTime
        drinks[i] = cur.timePoint
        heapq.heappush(heap, machine(cur.timePoint, cur.workTime))
    # print(washing(drinks, a, b, 0, 0))
    # print(washing_dp(drinks, n, a, b))
    return washing(drinks, a, b, 0, 0)


# 假设洗咖啡的机器没在washLine的时间点才有空
# a: 洗咖啡杯的机器洗一个杯子的时间
# b: 咖啡杯自然挥发的时间
# 函数定义：如果要洗完drinks[index...N-1]，返回最早完成所有事情的时间点
def washing(drinks, a, b, index, washLine):

    if index == len(drinks) - 1:
        return min(max(washLine, drinks[index] + a), drinks[index] + b)

    # 当前的咖啡杯放到机器里洗，什么时间点洗完
    wash = max(washLine, drinks[index] + a)
    # 洗完剩下所有咖啡最早的结束时间点
    next1 = washing(drinks, a, b, index + 1, wash)
    p1 = max(wash, next1)

    # 当前的咖啡杯自己挥发的结束时间点
    dry = drinks[index] + b
    # 洗完剩下所有咖啡最早的结束时间点
    next2 = washing(drinks, a, b, index + 1, washLine)
    p2 = max(dry, next2)

    return min(p1, p2)



# 动态规划版本的洗咖啡杯过程
def washing_dp(drinks, n, a, b):
    if a >= b:
        return drinks[-1] + b
    dp = np.zeros((n, drinks[-1] + n * a))

    for i in range(n):
        dp[n - 1][i] = min(max(i, drinks[n - 1] + a), drinks[n - 1] + b)

    for row in range(n - 2, -1, -1):
        washLine = drinks[row] + (row + 1) * a
        for col in range(washLine):
            wash = max(drinks[row], col) + a
            dp[row][col] = min(
                max(wash, dp[row + 1][wash]),
                max(drinks[row] + b, dp[row + 1][washLine]),
            )

    return dp[0][0]


if __name__ == "__main__":
    arrs = [2, 3, 5, 4]
    n = 10
    a = 2
    b = 3
    print(minTime(arrs, n, a, b))
