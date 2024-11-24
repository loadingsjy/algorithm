#
# * 632. 最小区间 - H
# 你有 k 个 非递减排列 的整数列表。找到一个 最小 区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
# 我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

# 示例 1：
# 输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# 输出：[20,24]
# 解释：
# 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
# 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
# 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
# 示例 2：
# 输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
# 输出：[1,1]

# 提示：
# nums.length == k
# 1 <= k <= 3500
# 1 <= nums[i].length <= 50
# -105 <= nums[i][j] <= 105
# nums[i] 按非递减顺序排列

from cmath import inf
from collections import defaultdict
from heapq import heapify, heapreplace
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        滑动窗口
        解题思路：
        首先将 k 组数据升序合并成一组，并记录每个数字所属的组，例如：
        [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
        合并升序后得到：
        [(0,1),(4,0),(5,2),(9,1),(10,0),(12,1),(15,0),(18,2),(20,1),(22,2),(24,0),(26,0),(30,2)]
        然后只看所属组的话，那么[1,0,2,1,0,1,0,2,1,2,0,0,2]
        按组进行滑窗，保证一个窗口的组满足k组后在记录窗口的最小区间值。
        """
        n = len(nums)
        temp = []
        for i, comb in enumerate(nums):
            temp.extend([(num, i) for num in comb])
        temp.sort(key=lambda x: x[0])

        left = 0
        occ = set()
        cnt = defaultdict(int)
        ans = [-inf, inf]
        for right, (num, i) in enumerate(temp):
            occ.add(i)
            cnt[i] += 1
            while left <= right and len(occ) == n:
                if num - temp[left][0] < ans[1] - ans[0] or (
                    num - temp[left][0] == ans[1] - ans[0] and temp[left][0] < ans[0]
                ):
                    ans = [temp[left][0], num]

                cnt[temp[left][1]] -= 1
                if cnt[temp[left][1]] == 0:
                    occ.remove(temp[left][1])
                left += 1
        return ans

    def smallestRange2(self, nums: List[List[int]]) -> List[int]:
        '''滑动窗口 灵写法'''
        pairs = sorted((x, i) for (i, arr) in enumerate(nums) for x in arr)
        ans_l, ans_r = -inf, inf
        empty = len(nums)
        cnt = [0] * empty
        left = 0
        for r, i in pairs:
            if cnt[i] == 0:  # 包含 nums[i] 的数字
                empty -= 1
            cnt[i] += 1
            while empty == 0:  # 每个列表都至少包含一个数
                l, i = pairs[left]
                if r - l < ans_r - ans_l:
                    ans_l, ans_r = l, r
                cnt[i] -= 1
                if cnt[i] == 0:  # 不包含 nums[i] 的数字
                    empty += 1
                left += 1
        return [ans_l, ans_r]

    def smallestRange3(self, nums: List[List[int]]) -> List[int]:
        """堆排序"""
        # 把每个列表的第一个元素入堆
        h = [(arr[0], i, 0) for i, arr in enumerate(nums)]
        heapify(h)

        ans_l = h[0][0]  # 第一个合法区间的左端点
        ans_r = r = max(arr[0] for arr in nums)  # 第一个合法区间的右端点
        while h[0][2] + 1 < len(nums[h[0][1]]):  # 堆顶列表有下一个元素
            _, i, j = h[0]
            x = nums[i][j + 1]  # 堆顶列表的下一个元素
            heapreplace(h, (x, i, j + 1))  # 替换堆顶
            r = max(r, x)  # 更新合法区间的右端点
            l = h[0][0]  # 当前合法区间的左端点
            if r - l < ans_r - ans_l:
                ans_l, ans_r = l, r
        return [ans_l, ans_r]


if __name__ == "__main__":
    sol = Solution()
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    print(sol.smallestRange(nums))
    print(sol.smallestRange2(nums))
    print(sol.smallestRange3(nums))
