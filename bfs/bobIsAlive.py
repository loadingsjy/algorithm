# 给定n*m的地图，bob的出生点为(i,j)，每次可以等概率向上下左右四个方向移动一步，问bob在走完k步后，继续生存的概率？(超出地图范围则为死亡)


def gcd(a, b):
    """求a,b的最大公约数"""
    return a if b == 0 else gcd(b, a % b)


def bob_walks_alive(n, m, row, col, k):
    if row < 0 or row >= n or col < 0 or col >= m:
        return 0
    if k == 0:
        return 1
    # 还没走完，row, col还在地图内
    live = (
        bob_walks_alive(n, m, row + 1, col, k - 1)
        + bob_walks_alive(n, m, row, col + 1, k - 1)
        + bob_walks_alive(n, m, row - 1, col, k - 1)
        + bob_walks_alive(n, m, row, col - 1, k - 1)
    )
    return live


def cal_alive_probability(n, m, i, j, k):
    total = 4**k
    live = bob_walks_alive(n, m, i, j, k)
    g = gcd(total, live)
    return (live / g) / (total / g)


if __name__ == "__main__":
    # n, m, i, j, k = map(int, input().split())
    m, n, i, j, k = 6, 7, 2, 3, 10
    print(
        "bob is alive with probability:{:.4%}".format(
            cal_alive_probability(n, m, i, j, k)
        )
    )
