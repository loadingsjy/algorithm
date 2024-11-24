# 找到数组中距离最远的两个相同的两个数字的距离


def max_distance(arr):

    max_distance = -1
    n = len(arr)
    index_dict = dict()
    for i, num in enumerate(arr):
        if num in index_dict:
            index_dict[num].append(i)
        else:
            index_dict[num] = [i]
    for num, indexs in index_dict.items():
        if len(indexs) > 1:
            max_distance = max(max_distance, max(indexs) - min(indexs))
    return max_distance


def max_distance2(arr):
    """哈希表"""
    ans = 0
    last_cur = dict()  # key: 数组元素 , value: 最早出现的索引
    for i, num in enumerate(arr):
        if num in last_cur:
            ans = max(ans, i - last_cur[num])
        else:
            last_cur[num] = i
    return ans


if __name__ == "__main__":

    arr = [1, 2, 3, 1, 4, 5, 2, 1]
    print(max_distance(arr))
    print(max_distance2(arr))
