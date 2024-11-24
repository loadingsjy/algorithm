#
# * 3254. 长度为 K 的子数组的能量值 I
# 给你一个长度为 n 的整数数组 nums 和一个正整数 k 。
# 一个数组的 能量值 定义为：
# 如果 所有 元素都是依次 连续 且 上升 的，那么能量值为 最大 的元素。
# 否则为 -1 。
# 你需要求出 nums 中所有长度为 k 的 数组的能量值。
# 请你返回一个长度为 n - k + 1 的整数数组 results ，其中 results[i] 是子数组 nums[i..(i + k - 1)] 的能量值。

# 示例 1：
# 输入：nums = [1,2,3,4,3,2,5], k = 3
# 输出：[3,4,-1,-1,-1]
# 解释：
# nums 中总共有 5 个长度为 3 的子数组：
# [1, 2, 3] 中最大元素为 3 。
# [2, 3, 4] 中最大元素为 4 。
# [3, 4, 3] 中元素 不是 连续的。
# [4, 3, 2] 中元素 不是 上升的。
# [3, 2, 5] 中元素 不是 连续的。


class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        ans = [-1] * (n - k + 1)

        length = 1
        for i in range(1, n):
            if nums[i - 1] + 1 == nums[i]:
                length += 1
            else:
                length = 1
            if i >= k-1:
                ans[i - k + 1] = nums[i] if length >= k else -1
        return ans
    
    def resultsArray2(self, nums: list[int], k: int) -> list[int]:
        '''灵神写法'''
        n = len(nums)
        cnt = 0
        ans = [-1] * (n - k + 1)
        for i in range(n):
            cnt = 1 if i == 0 or nums[i] - nums[i - 1] != 1 else cnt + 1
            if cnt >= k:
                ans[i - k + 1] = nums[i]
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 3, 2, 5]
    print(s.resultsArray(nums, 3))