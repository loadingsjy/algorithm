# 一个数组的 最小乘积 定义为这个数组中 最小值 乘以 数组的 和 。
# 比方说，数组 [3,2,5] （最小值是 2）的最小乘积为 2 * (3+2+5) = 2 * 10 = 20 。
# 给你一个正整数数组 nums ，请你返回 nums 任意 非空子数组 的最小乘积 的 最大值 。由于答案可能很大，请你返回答案对  10**9 + 7 取余 的结果。
# 请注意，最小乘积的最大值考虑的是取余操作 之前 的结果。题目保证最小乘积的最大值在 不取余 的情况下可以用 64 位有符号整数 保存。
# 子数组 定义为一个数组的 连续 部分。

# 示例 1：
# 输入：nums = [1,2,3,2]
# 输出：14
# 解释：最小乘积的最大值由子数组 [2,3,2] （最小值是 2）得到。
# 2 * (2+3+2) = 2 * 7 = 14 。
# 示例 2：
# 输入：nums = [2,3,3,1,2]
# 输出：18
# 解释：最小乘积的最大值由子数组 [3,3] （最小值是 3）得到。
# 3 * (3+3) = 3 * 6 = 18 。
# 示例 3：
# 输入：nums = [3,1,5,6,4,2]
# 输出：60
# 解释：最小乘积的最大值由子数组 [5,6,4] （最小值是 4）得到。
# 4 * (5+6+4) = 4 * 15 = 60 。


# 单调栈解决的问题：数组每个数的左/右边最近比它大/小的数字的index
# 双端队列解决的问题：实时获得窗口内的最大值和最小值


def maxSumMinProduct(nums):
    """单调栈：栈低放小的元素，栈顶放大的元素（允许有相等的元素），求数组每个数的左/右边最近比它（严格）小的数字的index"""
    stack = [[0]]
    n = len(nums)
    frist_left_smaller = [-1] * n  # 记录第 i 个元素左边的第一个比它小的元素的索引
    frist_right_smaller = [n] * n  # 记录第 i 个元素右边的第一个比它小的元素的索引

    for i, num in enumerate(nums):
        if not stack:
            stack.append([i])
        else:
            peek = nums[stack[-1][-1]]
            if peek < num:
                stack.append([i])
            elif peek == num:
                stack[-1].extend([i])
            elif peek > num:  # 先弹出比num大的栈顶元素，在加入栈中
                while stack and nums[stack[-1][-1]] > num:
                    for j in stack.pop():
                        frist_right_smaller[j] = i
                        if stack:
                            frist_left_smaller[j] = stack[-1][-1]
                if not stack:
                    stack.append([i])
                else:
                    if nums[stack[-1][-1]] == num:
                        stack[-1].extend([i])
                    elif nums[stack[-1][-1]] < num:
                        stack.append([i])

    # 弹出栈中剩余元素
    while stack:
        for i in stack.pop():
            if stack:
                frist_left_smaller[i] = stack[-1][-1]

    # print('nums: ',nums)
    # print("frist_left_smaller: ", frist_left_smaller)
    # print("frist_right_smaller: ", frist_right_smaller)

    # 计算最小乘积
    ans = float("-inf")
    for i in range(n):
        ans = max(
            ans, nums[i] * sum(nums[frist_left_smaller[i] + 1 : frist_right_smaller[i]])
        )

    # print('results: ',results)
    return ans % (10**9 + 7)


# 官方解答
def maxSumMinProduct_2(nums: list[int]) -> int:
    mod = 10**9 + 7

    n = len(nums)
    # 数组 left 初始化为 0，数组 right 初始化为 n-1
    # 设置为元素不存在时的特殊值
    left, right = [0] * n, [n - 1] * n
    # 单调栈
    s = list()
    for i, num in enumerate(nums):
        while s and nums[s[-1]] >= num:
            # 这里的 right 是非严格定义的，right[i] 是右侧最近的小于等于 nums[i] 的元素下标
            right[s[-1]] = i - 1
            s.pop()
        if s:
            # 这里的 left 是严格定义的，left[i] 是左侧最近的严格小于 nums[i] 的元素下标
            left[i] = s[-1] + 1
        s.append(i)

    # 前缀和
    pre = [0]
    for i, num in enumerate(nums):
        pre.append(pre[-1] + num)

    best = max((pre[right[i] + 1] - pre[left[i]]) * num for i, num in enumerate(nums))
    return best % mod


if __name__ == "__main__":

    nums = [2, 3, 5, 5, 7, 1, 6, 3]
    print(maxSumMinProduct(nums))  # 120
    print(maxSumMinProduct_2(nums))  # 120
    print()

    nums = [1, 2, 3, 2]
    print(maxSumMinProduct(nums))  # 14
    print(maxSumMinProduct_2(nums))  # 14
    print()

    nums = [2, 3, 3, 1, 2]
    print(maxSumMinProduct(nums))  # 18
    print(maxSumMinProduct_2(nums))  # 18
    print()

    nums = [3, 1, 5, 6, 4, 2]
    print(maxSumMinProduct(nums))  # 60
    print(maxSumMinProduct_2(nums))  # 60
    print()
