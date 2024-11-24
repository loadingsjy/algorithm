# 57. 插入区间

# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表 intervals，其中 intervals[i] = [starti, endi] 表示第 i 个区间的开始和结束，
# 并且 intervals 按照 starti 升序排列。
# 同样给定一个区间 newInterval = [start, end] 表示另一个区间的开始和结束。
# 在 intervals 中插入区间 newInterval，使得 intervals 依然按照 starti 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。
# 返回插入之后的 intervals。
# 注意 你不需要原地修改 intervals。你可以创建一个新数组然后返回它。


# 示例 1：
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
# 示例 2：
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

# 提示：
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals 根据 starti 按 升序 排列
# newInterval.length == 2
# 0 <= start <= end <= 105


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]):
        """另一种思路：二分查找末尾端点 第一个>=newInterval[0]的区间的末尾端点
        二分查找起始端点 第一个>newInterval[1]的区间的起始端点的前一个区间"""

        res = []
        l = len(intervals)
        i = 0
        # 一开始不重叠的区间直接加入答案
        while i < l and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        # 有重叠部分
        while i < l and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # 剩下的不重叠的区间直接加入答案
        while i < l:
            res.append(intervals[i])
            i += 1
        return res


if __name__ == "__main__":
    s = Solution()
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(s.insert(intervals, newInterval))
