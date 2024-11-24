# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
# 示例 1:
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
# 示例 2:
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]

# 此方法超时
# def productExceptSelf(nums: list[int]) -> list[int]:
#     n = len(nums)
#     answer = [0] * n
#     for i in range(0, n):
#         temp = nums[:i]+nums[i+1:]
#         if 0 in temp:
#             continue
#         answer[i] = reduce(lambda x, y: x * y, temp)
#     return answer


def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)

    rs_l, rs_r = [1] * n, [1] * n

    # 前缀积
    for i in range(1, n):
        rs_l[i] = rs_l[i - 1] * nums[i - 1]

    # 后缀积
    for i in range(n - 2, -1, -1):
        rs_r[i] = rs_r[i + 1] * nums[i + 1]

    # 乘在一起
    for i in range(n):
        rs_l[i] *= rs_r[i]

    return rs_l


def productExceptSelf(self, nums: list[int]) -> list[int]:
    """优化：空间复杂度O(1)"""
    length = len(nums)
    answer = [1] * length

    # answer[i] 表示索引 i 左侧所有元素的乘积
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]

    # R 为右侧所有元素的乘积
    # 刚开始右边没有元素，所以 R = 1
    R = 1
    for i in reversed(range(length)):
        # 对于索引 i，左边的乘积为 answer[i]，右边的乘积为 R
        answer[i] = answer[i] * R
        # R 需要包含右边所有的乘积，所以计算下一个结果时需要将当前值乘到 R 上
        R *= nums[i]

    return answer


def productExceptSelf(nums: list[int]) -> list[int]:
    """双指针解法：维护两个变量，beforeSum表示前缀和，afterSum表示后缀和"""
    n = len(nums)
    ans = [1] * n
    beforeSum, afterSum = 1, 1
    i, j = 0, n - 1
    while i < n:
        ans[i] *= beforeSum
        ans[j] *= afterSum
        beforeSum *= nums[i]
        afterSum *= nums[j]
        i += 1
        j -= 1
    return ans


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))  # [24,12,8,6]

    nums = [-1, 1, 0, -3, 3]
    print(productExceptSelf(nums))  # [0,0,9,0,0]
