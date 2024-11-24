# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

# 你返回所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

# 示例 1：

# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
# 示例 2：

# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
# 示例 3：

# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。


def threeSum(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    res = []
    n = len(nums)
    for i in range(n):  # 固定第一个值
        if i > 0 and nums[i] == nums[i - 1]:  # 跳过重复元素
            continue
        j, k = i + 1, n - 1  # 双指针
        temp = nums[i]
        while j < k:
            s = temp + nums[j] + nums[k]
            if s < 0:
                j += 1
            elif s > 0:
                k -= 1
            else:
                res.append((temp, nums[j], nums[k]))
                j += 1
                k -= 1
                # 跳过重复元素
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
    return list(set(res))  # 去重


def threeSum2(nums, target):
    """不重复的三个数，即保证a<b<c成立，时间复杂度：O(N^2)"""
    nums.sort()  # 先将nums从小到大排序
    n = len(nums)
    ans = []
    for frist in range(n - 2):  # 固定第一个值
        frist_num = nums[frist]
        if frist > 0 and nums[frist - 1] == frist_num:
            # 重复的不要
            continue
        if frist_num + nums[frist + 1] + nums[frist + 2] > target:
            # 最小的三个数相加都大于target了，后面没有答案了
            break
        if frist_num + nums[n - 2] + nums[n - 1] < target:
            # 第一个数加上最大的两个数都小于target了，后面没必要枚举了，不可能有等于target的了
            continue
        left, right = frist + 1, n - 1  # 双指针法
        while left < right:
            s = frist_num + nums[left] + nums[right]
            if s == target:
                ans.append([frist_num, nums[left], nums[right]])
                left += 1
                right -= 1
                # 跳过重复元素
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
    return ans


if __name__ == "__main__":  # 单元测试
    print(threeSum([-1, 0, 1, 2, -1, -4]))
    print(threeSum([0, 1, 1]))
    print(threeSum([0, 0, 0]))
    print()
    print(threeSum2([-1, 0, 1, 2, -1, -4], 0))
    print(threeSum2([0, 1, 1], 0))
    print(threeSum2([0, 0, 0], 0))
    print(threeSum2([1, 2, -2, -1], 0))
