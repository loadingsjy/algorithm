# 题目描述:
# 【羊、狼、农夫过河】
# 羊、狼、农夫都在岸边，当羊的数量小于狼的数量时，狼会攻击羊，农夫则会损失羊。农夫有一艘容量固定的船，能够承载固定数量的动物。要求求出不损失羊情况下将全部羊和狼运到对岸需要的最小次数。只计算农夫去对岸的次数，回程时农夫不会运送羊和狼。
# 备注：农夫在或农夫离开后羊的数量大于狼的数量时狼不会攻击羊。农夫自身不占用船的容量。

# 【输入描述】
# 第一行输入为M，N，X， 分别代表羊的数量，狼的数量，小船的容量。

# 【输出描述】
# 输出不损失羊情况下将全部羊和狼运到对岸需要的最小次数（若无法满足条件则输出0）。

# 【示例1】
# 输入: 5 3 3
# 输出: 3
# 说明:第一次运2只狼第二次运3只羊第三次运2只羊和1只狼

# 【示例2】
# 输入: 5 4 1
# 输出: 0
# 说明:如果找不到不损失羊的运送方案，输出0


def transport(M, N, X):

    MIN_TIMES = float("inf")

    # sheep,wolf,capacity为固定参数，代表羊的总数量、狼的总数量、船的容量
    # rest_sheep,rest_wolf为可变参数，代表当前岸边剩下的羊的数量和狼的数量（未运过河的）
    # times代表运送的次数，来回就是一趟（不考虑运回来）
    def dfs(sheep, wolf, capacity, rest_sheep, rest_wolf, times):
        nonlocal MIN_TIMES
        # 若可以一次性运走，结束了，注意等于号
        if capacity >= rest_sheep + rest_wolf:
            if times + 1 < MIN_TIMES:
                MIN_TIMES = times + 1
            return times + 1

        # 尝试运一部分狼一部分羊
        # 要上船的羊数量不可以超过岸上数量、也不可以超过船的容量
        # 要上船的狼的数量不可以超过岸上数量、也不可以超过船装了羊后的剩余的容量
        for i in range(min(rest_sheep, capacity) + 1):
            for j in range(min(rest_wolf, capacity - i) + 1):
                # 什么都不运
                if i + j == 0:
                    continue
                # 船离岸后，原来这岸，要么没有羊，要么羊比狼多; 对岸也要检查，不考虑回程带动物
                if (rest_sheep - i == 0 or rest_sheep - i > rest_wolf - j) and (
                    sheep - rest_sheep + i > wolf - rest_wolf + j):

                    result = dfs(sheep, wolf, capacity, rest_sheep - i, rest_wolf - j, times + 1)
                    if result != 0 and result < MIN_TIMES:
                        MIN_TIMES = result
        return 0

    dfs(M, N, X, M, N, 0)

    if MIN_TIMES == float("inf"):
        return -1
    else:
        return MIN_TIMES


# mO, n0分别表示剩余的羊、狼个数， X为船容量
# m1, n1分别表示运输到对岸的羊、狼个数，times 为次数
def transport_v2(m0, n0, x, m1, n1, times):
    # assert m0 + m1 == 5
    # assert n0 + n1 == 3
    global min_times
    # 若可以一次性运走，结束了,注意等于号
    if x >= m0 + n0:
        if times + 1 < min_times:
            min_times = times + 1
        return times + 1
    # 尝试运一部分狼一部分羊
    # 要上船的羊数量不可以超过岸上数量、也不可以超过船的容量
    for i in range(m0):
        if i > x:
            break
        # 要上船的狼的数量不可以超过岸上数量、也不可以超过船装了羊后的剩余的容量
        for j in range(n0):
            if i + j > x:
                break
            # 不可以不运
            if i + j == 0:
                continue
            # 船离岸后，原来这岸，要么没有羊，要么羊比狼多，才可以运;对岸也要检查，不考虑回程带动物
            if (m0 - i == 0 or m0 - i > n0 - j) and (m1 + i == 0 or m1 + i > n1 + j):
                # 运一次
                result = transport_v2(m0 - i, n0 - j, x, m1 + i, n1 + j, times + 1)
                # 如果获软J结果，和minTime比较， 但是不结束，继续检查
                if result < min_times and result != 0:
                    min_times = result

    return 0


if __name__ == "__main__":
    # sys.setrecursionlimit(1000000)  # 递归深度限制

    min_times = float("inf")
    print(transport(5, 3, 8))
    transport_v2(5, 3, 8, 0, 0, 0)
    print(min_times)
    print()

    min_times = float("inf")
    print(transport(10, 4, 4))
    transport_v2(10, 4, 4, 0, 0, 0)
    print(min_times)
    print()

    min_times = float("inf")
    print(transport(5, 3, 3))
    transport_v2(5, 3, 3, 0, 0, 0)
    print(min_times)
    print()

    min_times = float("inf")
    print(transport(5, 4, 1))
    transport_v2(5, 4, 1, 0, 0, 0)
    print(min_times)
    print()
