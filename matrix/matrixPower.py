# 矩阵的n次方
def matrixPower(mat, n):
    if len(mat) != len(mat[0]):
        raise ValueError("Matrix must be square")
    if n == 1:
        return mat
    identity_matrix = [
        [1 if i == j else 0 for j in range(len(mat))] for i in range(len(mat))
    ]
    res = identity_matrix
    t = mat
    while n != 0:
        if n & 1:
            res = matrixMultiply(res, t)
        t = matrixMultiply(t, t)
        n >>= 1
    return res


# 矩阵乘法
def matrixMultiply(mat1, mat2):
    rows1, cols1 = len(mat1), len(mat1[0])
    rows2, cols2 = len(mat2), len(mat2[0])
    if cols1 != rows2:
        return None
    result = [[0] * cols2 for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result


if __name__ == "__main__":
    # 示例
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n = 2
    print(matrixPower(mat, n))


