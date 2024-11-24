# 山脉数组的峰顶索引
# 给定一个长度为 n 的整数 山脉 数组 arr ，其中的值递增到一个 峰值元素 然后递减。
# 返回峰值元素的下标。
# 你必须设计并实现时间复杂度为 O(log(n)) 的解决方案。


# 示例 1：
# 输入：arr = [0,1,0]
# 输出：1
# 示例 2：
# 输入：arr = [0,2,1,0]
# 输出：1
# 示例 3：
# 输入：arr = [0,10,5,2]
# 输出：1


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            elif arr[mid] > arr[mid + 1]:
                right = mid - 1
        return left


if __name__ == "__main__":
    s = Solution()
    arr = [0, 10, 5, 2]
    print(s.peakIndexInMountainArray(arr))
