#
# * 1353. 最多可以参加的会议数目 - M
# 给你一个数组 events，其中 events[i] = [startDayi, endDayi] ，表示会议 i 开始于 startDayi ，结束于 endDayi 。
# 你可以在满足 startDayi <= d <= endDayi 中的任意一天 d 参加会议 i 。在任意一天 d 中只能参加一场会议。
# 请你返回你可以参加的 最大 会议数目。
# 提示：​​​​​​
# 1 <= events.length <= 10^5
# events[i].length == 2
# 1 <= startDayi <= endDayi <= 10^5

from typing import List
import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        1.将会议以开始时间从小到大进行排序
        2.构建会议结束时间的小根堆
        1) 遍历所有可以选择的日期
        2) 每次进行以下三个步骤
            ① 弹出过期会议
            ② 加入当天可以选择的会议
            ③ 弹出小根堆第一个元素，即选择最早结束的会议
        """
        events.sort(key=lambda x: x[0])
        start = events[0][0]
        end = max(list(zip(*events))[1])
        n = len(events)
        idx, ans = 0, 0

        heap = []
        heapq.heapify(heap)
        for day in range(start, end + 1):
            while idx < n and events[idx][0] <= day:
                heapq.heappush(heap, (events[idx][1], events[idx][0]))
                idx += 1
            while heap and heap[0][0] < day:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                ans += 1
        return ans


if __name__ == "__main__":
    events = [[1, 2], [2, 3], [3, 4]]
    print(Solution().maxEvents(events))

    events = [[1, 4], [4, 5], [2, 3], [3, 6]]
    print(Solution().maxEvents(events))
