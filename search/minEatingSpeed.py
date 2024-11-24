#
# * 875. 爱吃香蕉的珂珂 - M

# 珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。
# 珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。
# 如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。
# 珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
# 返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。

# 示例 1：
# 输入：piles = [3,6,7,11], h = 8
# 输出：4
# 示例 2：
# 输入：piles = [30,11,23,4,20], h = 5
# 输出：30
# 示例 3：
# 输入：piles = [30,11,23,4,20], h = 6
# 输出：23

# 提示：
# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """时间复杂的O(nlogk), k=max(plies), 额外空间复杂度O(1)"""

        def using_time(speed):
            """给定吃香蕉的速度，最少需要多少时间才能吃完"""
            time = 0
            for plie in piles:
                # time += ceil(plie / speed)
                time += (plie + speed - 1) // speed  # 向上取整的写法
            return time

        l, r = 1, max(piles)
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if using_time(mid) <= h:  # 达标
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
