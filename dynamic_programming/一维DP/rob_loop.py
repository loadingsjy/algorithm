def rob(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    # dp[i] 表示偷窃到第 i 个房屋的最大金额(包含第 i 个房屋)
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]


# 线性数组首位相连，所以可以将数组分为两部分，分别求解，然后取最大值
def rob_loop(nums):
    nums_1 = nums[:-1]
    nums_2 = nums[1:]
    return max(rob(nums_1), rob(nums_2))


if __name__ == "__main__":
    nums = [1, 2, 7, 9, 3, 1]
    print(rob_loop(nums))
