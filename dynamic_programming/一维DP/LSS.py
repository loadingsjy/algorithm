# 找出连续子数组的最大和


def maxSubArray(nums):
    # dp[i]表示以i结尾的子数组的最大和
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        # 延续和不延续两种情况
        dp[i] = max(nums[i], dp[i - 1] + nums[i])

    return max(dp)


if __name__ == "__main__":
    # test
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))  # 6
