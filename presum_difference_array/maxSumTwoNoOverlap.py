#
# * 1031. 两个非重叠子数组的最大和 - M
# 给你一个整数数组 nums 和两个整数 firstLen 和 secondLen，请你找出并返回两个非重叠 子数组 中元素的最大和，长度分别为 firstLen 和 secondLen 。
# 长度为 firstLen 的子数组可以出现在长为 secondLen 的子数组之前或之后，但二者必须是不重叠的。
# 子数组是数组的一个 连续 部分。

# 示例 1：
# 输入：nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
# 输出：20
# 解释：子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。
# 示例 2：
# 输入：nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
# 输出：29
# 解释：子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。
# 示例 3：
# 输入：nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
# 输出：31
# 解释：子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为 3。

# 提示：
# 1 <= firstLen, secondLen <= 1000
# 2 <= firstLen + secondLen <= 1000
# firstLen + secondLen <= nums.length <= 1000
# 0 <= nums[i] <= 1000

from itertools import accumulate


class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        """见图解
        对于有两个变量的题目，通常可以枚举其中一个变量，把它视作常量，从而转化成只有一个变量的问题。
        对于本题来说，就是枚举 b，把问题转化成计算 a 的最大元素和。
        """
        s = list(accumulate(nums, initial=0))  # nums 的前缀和
        ans = 0

        def f(firstLen: int, secondLen: int) -> None:
            nonlocal ans
            maxSumA = 0
            for i in range(firstLen + secondLen, len(s)):
                maxSumA = max(maxSumA, s[i - secondLen] - s[i - secondLen - firstLen])
                ans = max(ans, maxSumA + s[i] - s[i - secondLen])

        f(firstLen, secondLen)  # 左 a 右 b
        f(secondLen, firstLen)  # 左 b 右 a
        return ans

    def maxSumTwoNoOverlap2(self, nums: list[int], firstLen: int, secondLen: int):
        s = list(accumulate(nums, initial=0))  # nums 的前缀和
        ans = maxSumA = maxSumB = 0
        for i in range(firstLen + secondLen, len(s)):
            maxSumA = max(maxSumA, s[i - secondLen] - s[i - firstLen - secondLen])
            maxSumB = max(maxSumB, s[i - firstLen] - s[i - firstLen - secondLen])
            ans = max(
                ans, maxSumA + s[i] - s[i - secondLen], maxSumB + s[i] - s[i - firstLen]
            )
        return ans
