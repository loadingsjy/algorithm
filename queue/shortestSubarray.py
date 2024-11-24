#
# * 862. 和至少为 K 的最短子数组 - H
# 给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回 -1 。
# 子数组 是数组中 连续 的一部分。

# 示例 1：
# 输入：nums = [1], k = 1
# 输出：1
# 示例 2：
# 输入：nums = [1,2], k = 4
# 输出：-1
# 示例 3：
# 输入：nums = [2,-1,2], k = 3
# 输出：3
from collections import deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        """
        1.使用前缀和的差来计算子数组的和；

        2.使用一种数据结构，将当前前缀和i与最前面的前缀和j作差，如果满足>=k的条件，那么j在之后就可以不用看了。
        【因为即使后面也有满足条件的，长度也会更长，所以需要将j从前面弹出】；

        3.第2步完成了之后，当前的i也要放入数据结构，那么如果数据结构中有前缀和j比前缀和i大，j也可以不用看了。
        【因为即使后面有满足条件的，与i作差肯定也满足条件，并且长度更短，所以需要将大于等于i的从后面弹出】。

        总结：前面后面都要弹出，压入的元素满足单调性，所以使用单调队列。"""

        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        ans = n + 1
        q = deque()

        for i, num in enumerate(pre_sum):
            while q and pre_sum[i] - pre_sum[q[0]] >= k:  # 先看头部的前缀和是否满足答案
                if i - q[0] < ans:
                    ans = i - q[0]
                q.popleft()
            while (
                q and pre_sum[q[-1]] >= num
            ):  # 抛弃掉已经没有用的前缀和(长度更长，和更小)
                q.pop()
            q.append(i)
        return ans if ans != n + 1 else -1


if __name__ == "__main__":
    s = Solution()

    nums = [2, -1, 2]
    k = 3
    print(s.shortestSubarray(nums, k))

    nums = [
        11,
        47,
        97,
        35,
        -46,
        59,
        46,
        51,
        59,
        80,
        14,
        -6,
        2,
        20,
        96,
        1,
        18,
        74,
        -17,
        71,
    ]
    k = 282
    print(s.shortestSubarray(nums, k))
