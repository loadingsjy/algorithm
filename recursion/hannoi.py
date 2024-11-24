# 汉诺塔问题的递归解法


def hannoi(n):
    c = count(n, "左", "右", "中")  # c == (2^n-1)
    print("Total moves: " + str(c))
    dfs(n, "左", "右", "中")


def count(i, start, end, other):
    if i == 1:
        return 1

    return count(i - 1, start, other, end) + 1 + count(i - 1, other, end, start)


def dfs(i, start, end, other):
    """i代表1到i的所有圆盘，递归函数的含义，把1~i所有的圆盘从start圆柱上挪到end圆柱上，另外一个圆柱是other"""
    if i == 1:
        print("move 1 from " + str(start) + " to " + str(end))
        return

    dfs(i - 1, start, other, end)
    print("move " + str(i) + " from " + str(start) + " to " + str(end))
    dfs(i - 1, other, end, start)


if __name__ == "__main__":
    """n层汉诺塔问题最右移动轨迹一定是(2^n-1)步，f(n) = 2f(n-1) + 1"""
    n = 4
    hannoi(n)
