#
# * 18. 四数之和 - M
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 你可以按 任意顺序 返回答案 。

# 示例 1：
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 示例 2：
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]

# 提示：
# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for a in range(n - 3):  # 枚举第一个数
            x = nums[a]
            if a and x == nums[a - 1]:  # 跳过重复数字
                continue
            if x + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:  # 优化一
                break
            if x + nums[-3] + nums[-2] + nums[-1] < target:  # 优化二
                continue
            for b in range(a + 1, n - 2):  # 枚举第二个数
                y = nums[b]
                if b > a + 1 and y == nums[b - 1]:  # 跳过重复数字
                    continue
                if x + y + nums[b + 1] + nums[b + 2] > target:  # 优化一
                    break
                if x + y + nums[-2] + nums[-1] < target:  # 优化二
                    continue
                # 双指针枚举第三个数和第四个数
                c = b + 1
                d = n - 1
                while c < d:
                    s = x + y + nums[c] + nums[d]  # 四数之和
                    if s > target:
                        d -= 1
                    elif s < target:
                        c += 1
                    else:  # s == target
                        ans.append([x, y, nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:  # 跳过重复数字
                            c += 1
                        d -= 1
                        while d > c and nums[d] == nums[d + 1]:  # 跳过重复数字
                            d -= 1
        return ans
