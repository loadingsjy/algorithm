# 给一个二维数组nums，对于每一个元素num[i]，找出距离最近的且值相等的元素，输出横纵坐标差值的绝对值之和，如果没有等值元素，则输出-1。
# 例如：
# 输入数组nums为
# 0 3 5 4 2
# 2 5 7 8 3
# 2 5 4 2 4
# 对于num[0][0]=0，不存在相等的值。
# 对于num[0][1]=3，存在一个相等的值，最近的坐标为num[1][4]，最小距离为4。
# 对于num[0][2]=5，存在两个相等的值，最近的坐标为num[1][1]，故最小距离为2。
# ...
# 对于num[1][1]=5，存在两个相等的值，最近的坐标为num[2][1]，故最小距离为1。
# ...
# 故输出为
# -1 4  2  3  3
# 1  1 -1 -1  4
# 1  1  2  3  2

# 输入描述：
# 输入第一行为二维数组的行
# 输入第二行为二维数组的列
# 输入的数字以空格隔开。

# 输出描述:
# 数组形式返回所有坐标值。

# 示例1 输入输出示例仅供调试，后台判题数据一股不包含示例
# 输入
# 3
# 5
# 0 3 5 4 2
# 2 5 7 8 3
# 2 5 4 2 4
# 输出
# [[-1,4,2,3,3],
# [1,1,-1,-1,4],
# [1,1,2,3,2]]
# 备注：
# 1.针对数组num[i][j]，满足0＜i＜=100;0＜j＜=100。
# 2.对于每个数字，最多存在100个与其相等的数字。

from collections import defaultdict


def find_closest(coord, coord_list):
    min_distance = float("inf")
    res = []
    for x, y in coord_list:
        if (x, y) != coord:
            distance = abs(x - coord[0]) + abs(y - coord[1])
            if distance < min_distance:
                min_distance = distance
    if min_distance == float("inf"):
        return -1

    # for x, y in coord_list:
    #     if abs(x - coord[0]) + abs(y - coord[1]) == min_distance:
    #         res.append((x, y))
    return min_distance


def mindistance(mat):
    row = len(mat)
    col = len(mat[0])
    value_dict = defaultdict(list)

    ans = [[-1] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            value_dict[mat[i][j]].append((i, j))

    # print(value_dict)
    for _, coord_list in value_dict.items():
        if not coord_list:
            continue
        for x, y in coord_list:
            min_distance = find_closest((x, y), coord_list)
            ans[x][y] = min_distance
                    
    return ans

if __name__ == '__main__':
    
    mat = [[0, 3, 5, 4, 2],
           [2, 5, 7, 8, 3],
           [2, 5, 4, 2, 4]]
    
    print(mindistance(mat))
    
    
