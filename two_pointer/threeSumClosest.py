#
# * 16. 最接近的三数之和

# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
# 返回这三个数的和。
# 假定每组输入只存在恰好一个解。

# 示例 1：
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
# 示例 2：
# 输入：nums = [0,0,0], target = 1
# 输出：0
# 解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = float("inf")
        for i in range(n - 2):
            frist = nums[i]
            # 跳过重复元素
            if i > 0 and nums[i - 1] == frist:
                continue
            if (s := frist + nums[i + 1] + nums[i + 2]) > target:
                ans = s if abs(s - target) < abs(ans - target) else ans
                break
            if (s := frist + nums[-2] + nums[-1]) < target:
                ans = s if abs(s - target) < abs(ans - target) else ans
                continue
            left, right = i + 1, n - 1
            while left < right:
                s = frist + nums[left] + nums[right]
                ans = s if abs(s - target) < abs(ans - target) else ans
                if s < target:
                    left += 1
                    # 跳过重复元素
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif s > target:
                    right -= 1
                    # 跳过重复元素
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    return s
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    print(s.threeSumClosest(nums, target))
