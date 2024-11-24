# 位运算优化n皇后问题


def process(limit, colLim, leftDiaLim, rightDiaLim):
    """
    colLim: 限制位，表示当前皇后不能在的列，1表示不能放置，0表示可以放置
    leftDiaLim: 限制位，表示当前皇后不能在的左对角线，1表示不能放置，0表示可以放置
    rightDiaLim: 限制位，表示当前皇后不能在的右对角线，1表示不能放置，0表示可以放置
    """
    if colLim == limit:
        return 1
    pos = limit & (
        ~(colLim | leftDiaLim | rightDiaLim)
    )  # 找到可以放置的位置，1表示可以放置，0表示不可以放置
    mostRightOne = 0
    result = 0
    while pos != 0:
        mostRightOne = pos & (~pos + 1)  # 找到pos中最右侧的1
        pos = pos - mostRightOne
        result += process(
            limit,
            colLim | mostRightOne,
            (leftDiaLim | mostRightOne) << 1,
            (rightDiaLim | mostRightOne) >> 1,
        )
    return result


def n_queen(n):
    if n < 1 or n > 32:
        return 0
    limit = (1 << n) - 1  # 限制位，表示当前皇后不能在的列，1表示能放置，0表示不能放置
    return process(limit, 0, 0, 0)


if __name__ == "__main__":
    n = 5
    print(n_queen(n))
