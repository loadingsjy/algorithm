#
# * 连续数组
# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

# 示例 1:
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
# 示例 2:
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        """把0看作-1,把1看作1，子数组和为0 代表 0和1的数量相等"""
        # key: pre_sum   value: pre_sum最早出现的index
        mp = dict()
        mp[0] = -1
        pre_sum = 0
        ans = 0
        for i, num in enumerate(nums):
            pre_sum += -1 if num == 0 else num
            if pre_sum in mp:
                ans = max(ans, i - mp[pre_sum])
            else:
                mp[pre_sum] = i
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 0, 1, 1, 0, 0, 0]  # 0~5
    print(s.findMaxLength(nums))
