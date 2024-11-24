# * 321. 拼接最大数

# 给你两个整数数组 nums1 和 nums2，它们的长度分别为 m 和 n。数组 nums1 和 nums2 分别代表两个数各位上的数字。同时你也会得到一个整数 k。
# 请你利用这两个数组中的数字中创建一个长度为 k <= m + n 的最大数，在这个必须保留来自同一数组的数字的相对顺序。
# 返回代表答案的长度为 k 的数组。

# 示例 1：
# 输入：nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
# 输出：[9,8,6,5,3]
# 示例 2：
# 输入：nums1 = [6,7], nums2 = [6,0,4], k = 5
# 输出：[6,7,6,0,4]
# 示例 3：
# 输入：nums1 = [3,9], nums2 = [8,9], k = 3
# 输出：[9,8,9]


class Solution:
    """令数组 nums1的长度为 m，数组 nums2的长度为 n，则需要从数组 nums1中选出长度为 x 的子序列，以及从数组 nums2​中选出长度为 y 的子序列，其中 x+y=k，且满足 0≤x≤m 和 0≤y≤n。
    需要遍历所有可能的 x 和 y 的值，对于每一组 x 和 y 的值，得到最大数。在整个过程中维护可以通过拼接得到的最大数。
    对于每一组 x 和 y 的值，得到最大数的过程分成两步，第一步是分别从两个数组中得到指定长度的最大子序列，第二步是将两个最大子序列合并。

    第一步可以通过单调栈实现。单调栈满足从栈底到栈顶的元素单调递减，从左到右遍历数组，遍历过程中维护单调栈内的元素，需要保证遍历结束之后单调栈内的元素个数等于指定的最大子序列的长度。
    遍历结束之后，将从栈底到栈顶的元素依次拼接，即得到最大子序列。
    第二步需要自定义比较方法。首先比较两个子序列的当前元素，如果两个当前元素不同，则选其中较大的元素作为下一个合并的元素，否则需要比较后面的所有元素才能决定选哪个元素作为下一个合并的元素。
    """

    """官方答案"""

    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        m, n = len(nums1), len(nums2)
        maxSubsequence = [0] * k
        start, end = max(0, k - n), min(k, m)

        for i in range(start, end + 1):
            subsequence1 = self.getMaxSubsequence(nums1, i)
            subsequence2 = self.getMaxSubsequence(nums2, k - i)
            curMaxSubsequence = self.merge(subsequence1, subsequence2)
            if self.compare(curMaxSubsequence, 0, maxSubsequence, 0) > 0:
                maxSubsequence = curMaxSubsequence

        return maxSubsequence

    def getMaxSubsequence(self, nums: list[int], k: int) -> int:
        stack = [0] * k
        top = -1
        remain = len(nums) - k

        for i, num in enumerate(nums):
            while top >= 0 and stack[top] < num and remain > 0:
                top -= 1
                remain -= 1
            if top < k - 1:
                top += 1
                stack[top] = num
            else:
                remain -= 1

        return stack

    def merge(self, subsequence1: list[int], subsequence2: list[int]) -> list[int]:
        x, y = len(subsequence1), len(subsequence2)
        if x == 0:
            return subsequence2
        if y == 0:
            return subsequence1

        mergeLength = x + y
        merged = list()
        index1 = index2 = 0

        for _ in range(mergeLength):
            if self.compare(subsequence1, index1, subsequence2, index2) > 0:
                merged.append(subsequence1[index1])
                index1 += 1
            else:
                merged.append(subsequence2[index2])
                index2 += 1

        return merged

    def compare(self, subsequence1, index1, subsequence2, index2):
        x, y = len(subsequence1), len(subsequence2)
        while index1 < x and index2 < y:
            difference = subsequence1[index1] - subsequence2[index2]
            if difference != 0:
                return difference
            index1 += 1
            index2 += 1

        return (x - index1) - (y - index2)


if __name__ == "__main__":
    s = Solution()
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    print(s.maxNumber(nums1, nums1, k))
