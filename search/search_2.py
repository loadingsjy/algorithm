# 33. 搜索旋转排序数组
# 整数数组 nums 按升序排列，数组中的值 互不相同 。
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
# 例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

# 示例 1：
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# 示例 2：
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 示例 3：
# 输入：nums = [1], target = 0
# 输出：-1


from typing import List


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def is_blue(i):
            end = nums[-1]
            if nums[i] > end:
                return target > end and target <= nums[i]
            else:
                return target > end or target <= nums[i]

        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid - 1
            else:
                left = mid + 1
        if left == n or nums[left] != target:
            return -1
        return left

    def search2(self, nums: List[int], target: int) -> int:
        """核心思想:

        1.找到该数位于哪一段，把某个数 x 与最后一个数 nums[n−1] 比大小：
            如果 x>nums[n−1]，那么可以推出以下结论：
                nums 一定被分成左右两个递增段；
                第一段的所有元素均大于第二段的所有元素；
                x 在第一段。
            如果 x≤nums[n−1]，那么 x 一定在第二段。（或者 nums 就是递增数组，此时只有一段。）
        2.分别找到x和target的位于哪一段：
            如果 x 和 target 在不同的递增段：
            1)如果 target 在第一段（左），x 在第二段（右），说明 x 在 target 右边；
            2)如果 target 在第二段（右），x 在第一段（左），说明 x 在 target 左边。
            3)如果 x 和 target 在相同的递增段：
                比较 x 和 target 的大小即可。
        """
        l, r = 0, len(nums) - 1
        end = nums[-1]
        while l <= r:
            mid = (l + r) // 2
            x = nums[mid]
            if (target > end and x > end) or (target <= end and x <= end):
                if target > x:
                    l = mid + 1
                elif target < x:
                    r = mid - 1
                else:
                    return mid
            elif target > end and x <= end:
                r = mid - 1
            else:
                l = mid + 1
        return -1


if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(s.search(nums, target))
    print(s.search2(nums, target))
