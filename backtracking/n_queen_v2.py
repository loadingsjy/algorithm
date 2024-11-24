# n皇后问题

# 解决N皇后问题的时间复杂度是O(n!)，好的方法可以大量剪枝，大量优化常数时间

# 用数组表示路径的方法（经典、常数时间慢，不推荐）
# * 1.记录之前每一行的皇后放在了什么列
# * 2.来到第i行的时候，可以根据0..row-1行皇后的位置，判断能放哪些列
# * 3.把能放的列都尝试一遍，每次尝试修改路径数组表示当前的决策，后续返回的答案都累加返回


# n皇后问题（默认每行摆一个皇后），当前来到第row行，path数组：0 - row-1 前面已经选择的列号，后面填完皇后的方法数
def dfs(row, path, n):
    if row == n:
        return 1
    count = 0
    for col in range(n):
        if check(row, col, path):
            path[row] = col
            count += dfs(row + 1, path, n)
    return count


# 只判断0到row - 1行是否有冲突
# 返回row行皇后放在了col列，是否有效
def check(row, col, path):
    for i in range(row):
        # 当前皇后的列和之前的列不能一样，且不能共斜线
        if path[i] == col or abs(col - path[i]) == abs(row - i):
            return False
    return True


def n_queen(n):
    if n < 1:
        return 0
    path = [0] * n
    return dfs(0, path, n)


if __name__ == "__main__":
    print(n_queen(5))
