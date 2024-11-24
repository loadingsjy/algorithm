from bisect import bisect_left
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """二分查找"""
        n = len(intervals)
        intervals = list(map(tuple, intervals))
        index_dict = {interval: i for i, interval in enumerate(intervals)}
        intervals.sort(key=lambda x: x[0])
        ans = [-1] * n
        for x, y in intervals:
            src_idx = index_dict[(x, y)]
            idx = bisect_left(intervals, y, key=lambda x: x[0])
            if idx >= n:
                ans[src_idx] = -1
            else:
                ans[src_idx] = index_dict[intervals[idx]]
        return ans
    
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """双指针"""
        n = len(intervals)
        starts, ends = list(zip(*intervals))
        starts = sorted(zip(starts, range(n)))
        ends = sorted(zip(ends, range(n)))

        ans, j = [-1] * n, 0
        for end, id in ends:
            while j < n and starts[j][0] < end:
                j += 1
            if j < n:
                ans[id] = starts[j][1]
        return ans


if __name__ == "__main__":
    sol = Solution()
    intervals = [[3, 4], [2, 3], [1, 2]]
    print(sol.findRightInterval(intervals))
