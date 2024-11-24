#
# * 350. 两个数组的交集 II

# 给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。
# 返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。
# 示例 1：
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
# 示例 2:
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]
import collections


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """哈希表:
        首先遍历第一个数组，并在哈希表中记录第一个数组中的每个数字以及对应出现的次数，
        然后遍历第二个数组，对于第二个数组中的每个数字，如果在哈希表中存在这个数字，则将该数字添加到答案，并减少哈希表中该数字出现的次数。
        为了降低空间复杂度，首先遍历较短的数组并在哈希表中记录每个数字以及对应出现的次数，然后遍历较长的数组得到交集。
        时间复杂度：O(m+n)，空间复杂度：O(min(m,n))"""

        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        m = collections.Counter()
        for num in nums1:
            m[num] += 1

        intersection = list()
        for num in nums2:
            if (count := m.get(num, 0)) > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)

        return intersection

    def intersect2(self, nums1, nums2):
        """排序 + 双指针:
        首先对两个数组进行排序，然后使用两个指针遍历两个数组。
        初始时，两个指针分别指向两个数组的头部。
        每次比较两个指针指向的两个数组中的数字，如果两个数字不相等，则将指向较小数字的指针右移一位，
        如果两个数字相等，将该数字添加到答案，并将两个指针都右移一位。当至少有一个指针超出数组范围时，遍历结束。
        时间复杂度：O(mlogm+nlogn)，空间复杂度：O(min(m,n))"""
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        ans = []
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(s.intersect(nums1, nums2))
    print(s.intersect2(nums1, nums2))
