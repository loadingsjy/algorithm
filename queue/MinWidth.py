# 洛谷：P2698 浇花问题
# 老板需要你帮忙浇花。给出 N 滴水的坐标，y 表示水滴的高度，x 表示它下落到 x 轴的位置。

# 每滴水以每秒 1 个单位长度的速度下落。你需要把花盆放在 x 轴上的某个位置，
# 使得从被花盆接着的第 1 滴水开始，到被花盆接着的最后 1 滴水结束，之间的时间差至少为 D。

# 我们认为，只要水滴落到 x 轴上，与花盆的边沿对齐，就认为被接住。给出 N 滴水的坐标和 D 的大小，请算出最小的花盆的宽度 W。

from collections import deque
import sys


def MinWidth(mat, d):
    """滑动窗口 + 单调队列"""
    n = len(mat)
    queMax, queMin = deque(), deque()
    l = 0
    ans = float("inf")

    for r in range(n):
        while queMax and mat[queMax[-1]][1] <= mat[r][1]:
            queMax.pop()
        while queMin and mat[queMin[-1]][1] >= mat[r][1]:
            queMin.pop()

        queMax.append(r)
        queMin.append(r)

        while queMax and queMin and mat[queMax[0]][1] - mat[queMin[0]][1] >= d:
            ans = min(ans, mat[r][0] - mat[l][0])

            if l == queMin[0]:
                queMin.popleft()
            if l == queMax[0]:
                queMax.popleft()
            l += 1

    return -1 if ans == float("inf") else ans


if __name__ == "__main__":
    n, d = input().split()
    n = int(n)
    d = int(d)
    mat = [[0] * 2 for _ in range(n)]
    i = 0
    for line in sys.stdin:
        if not line.strip():
            break
        x, h = line.split()
        mat[i][0], mat[i][1] = int(x), int(h)
        i += 1
    mat.sort(key=lambda x: x[0])
    # print(mat)
    print(MinWidth(mat, d))


# 4 5
# 6 3
# 2 4
# 4 10
# 12 15
