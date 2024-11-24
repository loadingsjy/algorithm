# pre_cost: 之前已经花了多少钱，可变参数
# aim: 目标人气，固定参数
# add: 加2人气需要的钱，固定参数
# times: 乘2人气需要的钱，固定参数
# minus: 减2人气需要的钱，固定参数
# cur: 当前人气值，可变参数
# limitAim: 人气值大到什么程度就不需要尝试了，固定参数
# LimitCoin: 已经使用的钱大到什么程度了就不需要尝试了（一个平凡解)，固定参数
# 返回最小花费

import sys

sys.setrecursionlimit(1000000)  # 递归深度限制


def process(pre_cost, aim, add, times, minus, cur, limitAim, LimitCoin):
    if pre_cost > limitAim or pre_cost > LimitCoin or cur < 0:
        return sys.maxsize  # 超过限制，返回最大值
    if cur == aim:
        return pre_cost

    p1 = process(pre_cost + add, aim, add, times, minus, cur + 2, limitAim, LimitCoin)
    p2 = process(pre_cost + times, aim, add, times, minus, cur * 2, limitAim, LimitCoin)
    p3 = process(pre_cost + minus, aim, add, times, minus, cur - 2, limitAim, LimitCoin)

    return min(p1, p2, p3)


# start为当前人气值，end为目标人气值，start<=end，且均为偶数
def minCost(add, times, minus, start, end):
    if start > end:
        return -1
    if start == end:
        return 0
    return process(
        0, end, add, times, minus, start, end * 2, ((end - start) // 2) * add
    )


if __name__ == "__main__":
    add = 2
    times = 3
    minus = 1
    start = 2
    end = 10
    print(minCost(add, times, minus, start, end))
