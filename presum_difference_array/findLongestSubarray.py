#
# * 面试题 17.05. 字母与数字 - M

# 给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。
# 返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。

# 示例 1:
# 输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
# 输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
# 示例 2:
# 输入: ["A","A"]
# 输出: []
# 提示：
# array.length <= 100000


class Solution:
    def findLongestSubarray(self, array: list[str]) -> list[str]:
        """字母看成1，数字看成-1，求子数组和为0的最长子数组"""
        # n = len(array)
        max_left, ans = 0, -1
        pre_sum = 0
        mp = dict()
        mp[0] = -1  # key:前缀和  values:最早出现的index

        for i, ch in enumerate(array):
            pre_sum += 1 if ch.isalpha() else -1
            if pre_sum in mp:
                length = i - mp[pre_sum]
                if length > ans:
                    ans = length
                    max_left = mp[pre_sum]
            else:
                mp[pre_sum] = i
        return array[max_left : max_left + ans]
