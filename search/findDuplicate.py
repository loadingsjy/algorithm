# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

# 示例 1：
# 输入：nums = [1,3,4,2,2]
# 输出：2
# 示例 2：
# 输入：nums = [3,1,3,4,2]
# 输出：3
# 示例 3 :
# 输入：nums = [3,3,3,3,3]
# 输出：3


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """cnt[i]表示数组中<=i的数的数量，如果知道 cnt[] 数组随数字 i 逐渐增大具有单调性（即 target 前 cnt[i]≤i，target 后 cnt[i]>i），
        那么我们就可以直接利用二分查找来找到重复的数。"""

        n = len(nums)
        left = 0
        right = n - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            cnt = 0
            for i in range(n):
                cnt += 1 if nums[i] <= mid + 1 else 0
            if cnt <= mid + 1:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid + 1
        return ans

    def findDuplicate2(self, nums: list[int]) -> int:
        """我们对 nums 数组建图，每个位置 i 连一条 i→nums[i] 的边。
        由于存在的重复的数字 target，因此 target 这个位置一定有起码两条指向它的边，因此整张图一定存在环，
        且我们要找到的 target 就是这个环的入口，那么整个问题就等价于 142. 环形链表 II。"""

        low, fast = 0, 0
        low, fast = nums[low], nums[nums[fast]]
        while low != fast:
            low = nums[low]
            fast = nums[nums[fast]]
        fast = 0
        while fast != low:
            fast = nums[fast]
            low = nums[low]
        return low


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 4, 2, 2]
    print(s.findDuplicate(nums))
    print(s.findDuplicate2(nums))
