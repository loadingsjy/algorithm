# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

# 示例 1：
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2：
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。


def merge(intervals: list[list[int]]) -> list[list[int]]:
    if len(intervals) <= 1:
        return intervals
    intervals.sort(key=lambda x: x[0])
    result = []
    start, end = intervals[0]  # 记录当前区间的起始和终止位置
    for i in range(1, len(intervals)):
        if intervals[i][1] <= end:
            continue
        if intervals[i][0] <= end:
            end = max(intervals[i][1], end)
        else:
            result.append([start, end])
            end = intervals[i][1]
            start = intervals[i][0]
    result.append([start, end])

    return result


def merge2(self, intervals: list[list[int]]) -> list[list[int]]:
    """我们用数组 merged 存储最终的答案。
    首先，我们将列表中的区间按照左端点升序排序。然后我们将第一个区间加入 merged 数组中，并按顺序依次考虑之后的每个区间：
    如果当前区间的左端点在数组 merged 中最后一个区间的右端点之后，那么它们不会重合，我们可以直接将这个区间加入数组 merged 的末尾；
    否则，它们重合，我们需要用当前区间的右端点更新数组 merged 中最后一个区间的右端点，将其置为二者的较大值。"""
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        # 如果列表为空，或者当前区间与上一区间不重合，直接添加
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # 否则的话，我们就可以与上一区间进行合并
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))  # [[1,6],[8,10],[15,18]]

    intervals = [[1, 4], [4, 5]]
    print(merge(intervals))  # [[1,5]]

    intervals = [[1, 4], [2, 3]]
    print(merge(intervals))  # [[1,4]]

    intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    print(merge(intervals))  # [[1,10]]

    intervals = [[2, 3], [5, 5], [2, 2], [3, 4]]
    print(merge(intervals))  # [[2,4],[5,5]]
