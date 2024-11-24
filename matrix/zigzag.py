
# 请以zigzag的顺序打印矩阵

# 从（a,b)到（c,d）的对角线，如果from_up_to_down为True，则从上到下打印，否则从下到上打印
def get_diagonal(matrix, a, b, c, d, from_up_to_down = True):
    res = []
    if from_up_to_down:
        while a != c + 1:
            res.append(matrix[a][b])
            a += 1
            b -= 1
    else:
        while b != d - 1:
            res.append(matrix[c][d])
            c -= 1
            d += 1
    return res


# 以zigzag的顺序打印矩阵
def zigzagLevelOrder(matrix):
    
    ar = 0
    ac = 0
    
    br = 0
    bc = 0
    
    row = len(matrix) - 1
    col = len(matrix[0]) - 1
    res = []
    from_up_to_down = False
    while ar != row + 1:
        res.extend(get_diagonal(matrix, ar, ac, br, bc, from_up_to_down))
        # a点一直向右走，走到最右再往下走
        ar = ar + 1 if ac == col else ar
        ac = ac if ac == col else ac + 1
        
        # b点一直向下走，走到最下再往左走
        bc = bc + 1 if br == row else bc
        br = br if br == row else br + 1
        
        from_up_to_down = not from_up_to_down
    return res


if __name__ == '__main__':
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    print(zigzagLevelOrder(matrix))
    
    
    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    print(zigzagLevelOrder(matrix))
    
