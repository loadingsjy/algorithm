# 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
# 不占用额外内存空间能否做到？


# 示例 1:
# 给定 matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]


# 顺时针得到以（x1,y1）为左上角，（x2,y2）为右下角的矩阵的边界
def get_board(matrix, x1, y1, x2, y2):

    if x1 == x2:
        return matrix[x1][y1 : y2 + 1]
    if y1 == y2:
        return matrix[x1 : x2 + 1][y1]

    res = []
    res.extend(matrix[x1][y1 : y2 + 1])
    res.extend(matrix[x1 + 1 : x2 + 1][y2])
    res.extend(matrix[x2][y2 - 1 : y1 - 1 : -1])
    res.extend(matrix[x2 - 1 : x1 : -1][y1])

    return res


def rotate(matrix):
    a = 0
    b = 0
    c = len(matrix) - 1
    d = len(matrix[0]) - 1
    while a < c:
        rotate_edge(matrix, a, b, c, d)
        a += 1
        b += 1
        c -= 1
        d -= 1
    return matrix


# 旋转以（x1,y1）为左上角，（x2,y2）为右下角的矩阵的边界
def rotate_edge(matrix, a, b, c, d):
    temp = 0
    for i in range(d - b):
        temp = matrix[a][b + i]
        matrix[a][b + i] = matrix[c - i][b]
        matrix[c - i][b] = matrix[c][d - i]
        matrix[c][d - i] = matrix[a + i][d]
        matrix[a + i][d] = temp


if __name__ == "__main__":

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate(matrix))
    
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(rotate(matrix))
