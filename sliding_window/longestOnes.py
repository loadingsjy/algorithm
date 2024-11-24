# 最大连续1的个数
# 给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。
# 示例 1：
# 输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释：[1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。
# 示例 2：
# 输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。
import bisect


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        """滑动窗口，允许窗口内最多出现2个0，不限1的个数"""
        zero_count = 0
        left = 0
        ans = -1
        for right, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

    def longestOnes2(self, nums: list[int], k: int) -> int:
        """前缀和 + 二分查找：
        对于任意的右端点 right，希望找到最小的左端点 left，使得 [left,right] 包含不超过 k 个 0。
        只要我们枚举所有可能的右端点，将得到的区间的长度取最大值，即可得到答案。"""
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i, num in enumerate(nums):
            pre_sum[i + 1] = pre_sum[i] + (1 - num)

        ans = 0
        for right in range(n):
            left = bisect.bisect_left(pre_sum, pre_sum[right + 1] - k)
            ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    print(s.longestOnes(nums, k))
    print(s.longestOnes2(nums, k))
    print()

    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    print(s.longestOnes(nums, k))
    print(s.longestOnes2(nums, k))
