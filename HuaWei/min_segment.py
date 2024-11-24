# 给定坐标轴上的一组线段，线段的起点和终点均为整数并且长度不小于，请你从中找出最少得线段数量，这些线段可以覆盖所有的线段。

import functools


def min_segment(segments):
    if len(segments) == 1:
        return 1
    ans = 1
    segments.sort(key=lambda x: x[0])
    left = segments[0][0]
    right = segments[0][1]
    flag = 0
    for l, r in segments[1:]:
        if l > right:
            ans += 1
            left = l
            right = r
            flag = 0
        if r <= right:
            flag = 0
            continue

        if left <= l <= right and r > right:
            if flag == 0:
                ans += 1
                flag = 1
            else:
                continue
    return ans


# def find_min_line(ranges, index, ans, start, min_num, total_length):
#     # 完全覆盖
#     if ranges[index][1] - start >= total_length:
#         min_num = min(min_num, ans)
#         return
#     temp = 0
#     for i in range(index + 1, len(ranges)):
#         # 找出剩余线段中坐瑞点小子起始线段的右端点
#         if ranges[i][0] <= ranges[index][1]:
#             if ranges[i][1] > ranges[temp][1]:
#                 temp = i
#         else:
#             break
#         if temp != 0:
#             find_min_line(ranges, temp, ans + 1, start, min_num, total_length)


# def comp(a, b):
#     if a[0] == b[0]:
#         return b[1] - a[1]
#     else:
#         return b[0] - a[0]


if __name__ == "__main__":
    # 处理输入
    # m = int(input())
    # ranges = []
    # for i in range(m):
    #     ranges.append([int(x) for x in input().split(",")])
    # ranges.sort(key=functools.cmp_to_key(comp))
    # total_length = ranges[len(ranges)-1][1] - ranges[0][0]
    # #区间起点
    # start = 0
    # min_num = len( ranges)
    # for i in range(m):
    #     start = ranges[1][0]
    # find_min_line(ranges, i, 1, start, min_num, total_length)
    # print(min_num)

    segments = [(1, 4), (2, 5), (3, 6)]
    print(min_segment(segments))

    segments = [(1, 2), (2, 5), (3, 6)]
    print(min_segment(segments))
