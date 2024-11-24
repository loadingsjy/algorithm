#
# * 137. 只出现一次的数字 II - M

# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
# 你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。

# 示例 1：
# 输入：nums = [2,2,3,2]
# 输出：3
# 示例 2：
# 输入：nums = [0,1,0,1,0,1,99]
# 输出：99

# 提示：
# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    ans -= 1 << i
                else:
                    ans |= 1 << i
        return ans

    def singleNumber2(self, nums: list[int]) -> int:

        def findLessM(arr, k):
            """更通用的方法：已知数组中只有1种数字出现小于k次，
            其他数都出现了k次，返回出现次数小于k的那种数"""
            cnts = [0] * 32
            for num in arr:
                for i in range(32):
                    cnts[i] += (num >> i) & 1
            ans = 0
            for i in range(32):
                if cnts[i] % k:
                    if i == 31:  # Python 这里对于最高位需要特殊判断
                        ans -= 1 << i
                    else:
                        ans |= 1 << i
            return ans

        return findLessM(nums, 3)


if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 3, 2]
    print(s.singleNumber(nums))
    print(s.singleNumber2(nums))

    nums = [0, 1, 0, 1, 0, 1, 99]
    print(s.singleNumber(nums))
    print(s.singleNumber2(nums))
