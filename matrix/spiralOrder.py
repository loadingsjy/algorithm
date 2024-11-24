# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]

# 示例 2：
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    row_length = len(matrix)
    col_length = len(matrix[0])
    result = []
    top, bottom, left, right = 0, row_length - 1, 0, col_length - 1
    while top <= bottom and left <= right:
        # 从左到右
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        # 从上到下
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        # 从右到左
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        # 从下到上
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result
