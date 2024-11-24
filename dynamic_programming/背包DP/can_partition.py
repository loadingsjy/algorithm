# 分割等和子集
# 可以看成是 0-1 背包问题，即是否存在一种方案，将数组中的元素分割成两个子集，使得这两个子集的元素和相等。

# 状态转移方程：dp[i][j] 表示前 i 个元素能否分割成两个子集，使得这两个子集的元素和为 j。
# 如果 j < nums[i - 1]，则 dp[i][j] = dp[i - 1][j]，即不选择第 i 个元素。
# 如果 j >= nums[i - 1]，则 dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]，即选择第 i 个元素。
# 最后，dp[len(nums)][target_sum] 即为是否存在一种方案，将数组分割成两个子集，使得这两个子集的元素和相等。


def canPartition_recurive(nums):
    _sum = sum(nums)
    div, mod = divmod(_sum, 2)
    if mod or max(nums) > div:
        return False
    nums.sort(reverse=True)
    target = [div] * 2
    return dfs(nums, 0, target)


# 把num[0...index]物品放入target背包中，能否正好放
def dfs(nums, index, target):
    for i in range(2):
        if target[i] >= nums[index]:
            target[i] -= nums[
                index
            ]  # 将nums[index]分别尝试加入到target[0]或target[1]中
            if target[i] == 0 or dfs(nums, index + 1, target):
                return True
            else:
                target[i] += nums[index]
    return False


def can_partition_dp(nums):
    """问题转化为能否从nums选出一些数字正好能装满容量为sum//2的背包中"""
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    target_sum = total_sum // 2
    # dp[i][j]表示nums[0...i]是否可以正好装进容量为j的背包中
    dp = [[False] * (target_sum + 1) for _ in range(len(nums) + 1)]

    for i in range(len(nums) + 1):
        dp[i][0] = True

    for i in range(1, len(nums) + 1):
        for j in range(1, target_sum + 1):
            if j < nums[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
    return dp[len(nums)][target_sum]


def can_partition_improved(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    target_sum = total_sum // 2

    dp = [False] * (target_sum + 1)
    dp[0] = True
    if nums[0] <= target_sum:
        dp[nums[0]] = True

    for i in range(1, len(nums) + 1):
        for j in range(target_sum, -1, -1):
            if j >= nums[i - 1]:
                dp[j] = dp[j] or dp[j - nums[i - 1]]

        # if dp[target_sum]:
        #     return True

    return dp[target_sum]


# 输入：nums = [1, 5, 11, 5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11]。

# 输入：nums = [1, 2, 3, 4, 5]
# 输出：false
# 解释：数组不能分割成两个和相等的子集。
if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print(canPartition_recurive(nums))
    print(can_partition_dp(nums))
    print(can_partition_improved(nums))
    print()
    nums = [1, 2, 3, 4, 5]
    print(canPartition_recurive(nums))
    print(can_partition_dp(nums))
    print(can_partition_improved(nums))
