# 找到k个最近的元素
# 给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。
# 整数 a 比整数 b 更接近 x 需要满足：
# |a - x| < |b - x| 或者
# |a - x| == |b - x| 且 a < b

# 示例 1：
# 输入：arr = [1,2,3,4,5], k = 4, x = 3
# 输出：[1,2,3,4]
# 示例 2：
# 输入：arr = [1,2,3,4,5], k = 4, x = -1
# 输出：[1,2,3,4]

"""先二分查找>=x的第一个数，如果是数组的第一个数，则返回前k个数；如果没找到，则返回最后k个数；
如果是中间的数，则用两个指正向两边扩散，每次比较左右指针和x的距离"""

import bisect
import math


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        n = len(arr)
        # 在数组中二分查找第一个大于等于x的数
        bound = bisect.bisect_left(arr, x)
        if bound == 0:
            return arr[:k]
        if bound == n:
            return arr[n - k :]

        # ans_left, ans_right = bound - 1, bound
        ans = []

        left = bound - 1
        right = bound
        left_dis = abs(x - arr[left])
        right_dis = abs(arr[right] - x)

        while len(ans) < k:
            if left_dis <= right_dis:
                ans.insert(0, arr[left])
                left -= 1
                if left < 0:
                    left_dis = float("inf")
                else:
                    left_dis = abs(x - arr[left])
            elif left_dis > right_dis:
                ans.append(arr[right])
                right += 1
                if right >= n:
                    right_dis = float("inf")
                else:
                    right_dis = abs(arr[right] - x)
        return ans

    def findClosestElements2(self, arr: list[int], k: int, x: int) -> list[int]:
        """时间复杂度：O(logn+k)，其中 n 是数组 arr 的长度。二分查找需要 O(logn)，双指针查找需要 O(k)。
        空间复杂度：O(1)。返回值不计入空间复杂度。"""
        right = bisect.bisect_left(arr, x)
        left = right - 1
        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= len(arr) or x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left + 1 : right]

    def findClosestElements3(self, arr: list[int], k: int, x: int) -> list[int]:
        """时间复杂度O(n - k)"""
        n = len(arr)
        left = 0  # 滑动窗口左边界
        for right in range(k, n):  # 滑动窗口右边界从k开始，大小为k
            # 如果右边界距离目标值更近，则左边界向右移动一步
            # 另外为了防止窗口在数值相同处停滞，当右边界值等于左边界时，窗口也向右滑动一步
            if abs(arr[right] - x) < abs(arr[left] - x) or arr[right] == arr[left]:
                left += 1
            else:  # 当右边界距离大于等于左边界距离时，就退出循环
                break

        return arr[left : left + k]  # 返回以left为左边界，大小为k的滑动窗口

    def findClosestElements_sort(self, arr: list[int], k: int, x: int) -> list[int]:
        """时间复杂度：O(nlogn)，其中 n 是数组 arr 的长度。排序需要 O(nlogn)。
        空间复杂度：O(logn)。返回值不计算时间复杂度。排序需要 O(logn) 的栈空间。"""
        arr.sort(key=lambda v: abs(v - x))  # 只需按照距离排序即可
        return sorted(arr[:k])


if __name__ == "__main__":
    s = Solution()
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    print(s.findClosestElements(arr, k, x))
    print(s.findClosestElements2(arr, k, x))
    print(s.findClosestElements3(arr, k, x))
    print(s.findClosestElements_sort(arr, k, x))
    print()

    arr = [-2, -1, 1, 2, 3, 4, 5]
    k = 7
    x = 3
    print(s.findClosestElements(arr, k, x))
    print(s.findClosestElements2(arr, k, x))
    print(s.findClosestElements3(arr, k, x))
    print(s.findClosestElements_sort(arr, k, x))
    print()
