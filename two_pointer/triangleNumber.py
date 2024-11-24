#
# * 611. 有效三角形的个数 - M
# 给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。
# 示例 1:
# 输入: nums = [2,2,3,4]
# 输出: 3
# 解释:有效的组合是:
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
# 示例 2:
# 输入: nums = [4,2,3,4]
# 输出: 4


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        """两边之和大于第三边
        由于不能重复统计，不妨规定三角形的三条边1 <= a<= b <= c，满足三角形的条件即为a + b > c"""
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        ans = 0
        for i in range(n - 1, 1, -1):
            thrid = nums[i]  # 先确定第三边（最大边）
            left, right = 0, i - 1
            # 最小的两个数相加都大于第三边，那么从left到right任取两个数都满足答案
            # if nums[0] + nums[1] > thrid:
            #     ans += (i - 1) * i // 2
            #     continue

            # 如果最小的两个数相加都大于第三边，
            # 说明从 nums[0] 到 nums[i] 中任选三个数 a,b,c 都满足 a+b>c，即C i+1取 3= (i+1)i(i−1)/6
            if nums[0] + nums[1] > thrid:
                ans += (i - 1) * i * (i + 1) // 6
                break
            # 如果最大的两个数相加都小于等于第三边，那么从left到right任取两个数都<=thrid，不满足答案
            if nums[right] + nums[right - 1] <= thrid:
                continue
            while left < right:
                while left < right and nums[left] + nums[right] <= thrid:
                    left += 1
                ans += right - left
                right -= 1
        return ans

    def triangleNumber2(self, nums: list[int]) -> int:
        """灵神版本"""
        nums.sort()
        ans = 0
        for k in range(len(nums) - 1, 1, -1):
            c = nums[k]
            # 在执行双指针之前，如果发现最小的 a 和 b 相加大于 c，说明从 nums[0] 到 nums[k] 中任选三个数 a,b,c 都满足 a+b>c，
            # 那么直接把 C k+1取 3= (k+1)k(k−1)/6加入答案，退出外层循环。这是为什么要倒序枚举 k 的原因（正序枚举没法退出外层循环）。
            if nums[0] + nums[1] > c:  # 优化一
                ans += (k + 1) * k * (k - 1) // 6
                break
            # 在执行双指针之前，如果发现最大的 a 和 b 相加小于 c，说明不存在 a+b>c，不执行双指针，继续外层循环。
            if nums[k - 2] + nums[k - 1] < c:  # 优化二
                continue
            i = 0  # a=nums[i]
            j = k - 1  # b=nums[j]
            while i < j:
                if nums[i] + nums[j] > c:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 3, 4]
    print(s.triangleNumber(nums))
    print(s.triangleNumber2(nums))

    nums = [4, 2, 3, 4]
    print(s.triangleNumber(nums))
    print(s.triangleNumber2(nums))
