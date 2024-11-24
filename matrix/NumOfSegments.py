# 给定一张图片，二维矩阵，每个元素代表像素的灰度值，1代表黑色，0代表白色。
# 我们要计算出这个图片中有多少个连续的黑色像素块。

# 思路：
# 遍历矩阵，遇到黑色像素，则记录下来，如果遇到白色像素，则判断之前记录的黑色像素块是否连续，如果是连续的，则将该快标记为2并继续遍历，如果不是连续的，则计数器加1。
# 时间复杂度：O(mn)，遍历矩阵一次。
# 空间复杂度：O(1)，只用常数的额外空间。


def infect(matrix, i, j, n, m):
    if i < 0 or j < 0 or i >= n or j >= m or matrix[i][j] != 1:
        return

    matrix[i][j] = 2
    infect(matrix, i - 1, j, n, m)  # 上
    infect(matrix, i + 1, j, n, m)  # 下
    infect(matrix, i, j - 1, n, m)  # 左
    infect(matrix, i, j + 1, n, m)  # 右
    infect(matrix, i - 1, j - 1, n, m)  # 左上
    infect(matrix, i - 1, j + 1, n, m)  # 左下
    infect(matrix, i + 1, j - 1, n, m)  # 右上
    infect(matrix, i + 1, j + 1, n, m)  # 右下


def countIslands(matrix: list[list[int]]) -> int:
    n, m = len(matrix), len(matrix[0])
    result = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                result += 1
                # 感染过程，将连通块所有元素标记为2
                infect(matrix, i, j, n, m)
    return result


if __name__ == "__main__":
    matrix = [
        [0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 1],
        [0, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 1],
    ]
    print(countIslands(matrix))  # Output: 3
