# 位运算优化n皇后问题

# 用位运算的方法（巧妙、常数时间快，推荐）
# int col   : 0..i-1行皇后放置的位置因为正下方向延伸的原因，哪些列不能再放皇后
# int left  : 0..i-1行皇后放置的位置因为左下方向延伸的原因，哪些列不能再放皇后
# int right : 0..i-1行皇后放置的位置因为右下方向延伸的原因，哪些列不能再放皇后
# 根据col、left、right，用位运算快速判断能放哪些列
# 把能放的列都尝试一遍，每次尝试修改3个数字表示当前的决策，后续返回的答案都累加返回

import time

from n_queen import Solution


def dfs(limit, colLim, leftDiaLim, rightDiaLim):
    """
    limit：固定变量，表示最后有几位1就是几皇后问题
    colLim: 限制位，表示当前皇后不能在的列，1表示不能放置，0表示可以放置
    leftDiaLim: 限制位，表示当前皇后不能在的左对角线，1表示不能放置，0表示可以放置
    rightDiaLim: 限制位，表示当前皇后不能在的右对角线，1表示不能放置，0表示可以放置
    """
    if colLim == limit:
        return 1
    # 总限制取反与上limit：找到可以放置的位置，1表示可以放置，0表示不可以放置
    candidates = limit & (~(colLim | leftDiaLim | rightDiaLim))
    mostRightOne = 0
    ans = 0
    while candidates != 0:  # 每次提取candidates最右侧的1进行尝试
        mostRightOne = candidates & -candidates  # 找到pos中最右侧的1
        # candidates = candidates - mostRightOne
        # candidates &= candidates - 1
        candidates ^= mostRightOne
        ans += dfs(
            limit,
            colLim | mostRightOne,
            (leftDiaLim | mostRightOne) << 1,
            (rightDiaLim | mostRightOne) >> 1,
        )
    return ans


def n_queen(n):
    if n < 1 or n > 32:
        return 0
    # 总限制位，表示当前皇后不能在的列，1表示能放置，0表示不能放置
    limit = ((1 << n) - 1) & 0xFFFFFFFF
    return dfs(limit, 0, 0, 0)


if __name__ == "__main__":
    # n = 5
    # print(n_queen(n))

    # 解决 12 皇后问题:
    # 方法1(递归)使用时间      ： 3.33s
    # 方法2(位运算优化)使用时间： 0.18s
    # 解决 15 皇后问题:
    # 方法2(位运算优化)使用时间： 36.11s

    n = 12
    print("解决", n, "皇后问题:")
    start = time.time()
    res1 = Solution().solveNQueens3(n)
    end = time.time()
    print("方法1(递归)使用时间      ： {:.2f}s".format(end - start))

    start = time.time()
    res1 = n_queen(n)
    end = time.time()
    print("方法2(位运算优化)使用时间： {:.2f}s".format(end - start))

    n = 15
    print("解决", n, "皇后问题:")

    start = time.time()
    res1 = n_queen(n)
    end = time.time()
    print("方法2(位运算优化)使用时间： {:.2f}s".format(end - start))
