# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 找出该数组中满足其总和大于等于 target 的长度最小的子数组
#  [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

# 示例 1：
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 示例 2：
# 输入：target = 4, nums = [1,4,4]
# 输出：1
# 示例 3：
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0


# 暴力法
# def minSubArrayLen(target: int, nums: list[int]) -> int:
#     n = len(nums)
#     for window in range(1, n + 1):
#         for i in range(n - window + 1):
#             if sum(nums[i: i + window]) >= target:
#                 return window
#     return 0


# 优化：滑动窗口
# 我们可以用两个指针 left 和 right 维护一个窗口，窗口的左边界是 left，右边界是 right。
# 我们用 right 指针向右移动，直到窗口的和大于等于 target，此时我们更新答案 res。
# 然后我们用 left 指针向右移动，直到窗口的和小于 target，此时我们更新窗口的左边界。
# 重复上述过程，直到 right 指针到达数组末尾。
# 时间复杂度：O(n)
# 空间复杂度：O(1)

import bisect


def minSubArrayLen(target: int, nums: list[int]) -> int:
    n = len(nums)
    left = 0
    right = -1
    res = n + 1
    s = 0
    while right + 1 < n:
        s += nums[right + 1]
        right += 1
        while s >= target:
            res = min(res, right - left + 1)
            s -= nums[left]
            left += 1
    return res if res != n + 1 else 0


def minSubArrayLen2(target: int, nums: list[int]) -> int:
    """滑动窗口"""
    n = len(nums)
    s, ans = 0, n + 1
    right = -1
    for left in range(n):
        if left > 0:
            s -= nums[left - 1]
        while right + 1 < n and s < target:
            s += nums[right + 1]
            right += 1
        if s >= target:
            ans = min(right - left + 1, ans)
    return ans if ans != n + 1 else 0


def minSubArrayLen3(target: int, nums: list[int]) -> int:
    """前缀和 + 二分查找"""
    if not nums:
        return 0

    n = len(nums)
    ans = n + 1
    sums = [0]
    for i in range(n):
        sums.append(sums[-1] + nums[i])

    for i in range(1, n + 1):
        s = target + sums[i - 1]
        # 找到前缀和数组中第一个 >= target + sums[i - 1]的索引bound，这样从i到bound的和一定>=target
        bound = bisect.bisect_left(sums, s)
        if bound != len(sums):
            ans = min(ans, bound - (i - 1))

    return 0 if ans == n + 1 else ans


if __name__ == "__main__":
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(minSubArrayLen(target, nums))  # Output: 2
    print(minSubArrayLen2(target, nums))
    print(minSubArrayLen3(target, nums))
    print()
    target = 4
    nums = [1, 4, 4]
    print(minSubArrayLen(target, nums))  # Output: 1
    print(minSubArrayLen2(target, nums))  # Output: 2
    print(minSubArrayLen3(target, nums))
    print()
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    print(minSubArrayLen(target, nums))  # Output: 0
    print(minSubArrayLen2(target, nums))  # Output: 2
    print(minSubArrayLen3(target, nums))
