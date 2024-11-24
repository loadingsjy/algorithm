# 给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：
# 选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
# 重复这个过程恰好 k 次。可以多次选择同一个下标 i 。
# 以这种方式修改数组后，返回数组 可能的最大和 。

# 示例 1：
# 输入：nums = [4,2,3], k = 1
# 输出：5
# 解释：选择索引 1 ，nums[1] 变为 -2 。数组变为 [4,-2,3] 。
# 再选择索引 2 ，nums[2] 变为 -3 。数组变为 [4,-2,-3] 。
# 最后，数组的和为 4 + (-2) + (-3) = 5 。

# 示例 2：
# 输入：nums = [3,-1,0,2], k = 3
# 输出：6
# 解释：选择索引 0 ，nums[0] 变为 -3 。数组变为 [-3,-1,0,2] 。
# 再选择索引 1 ，nums[1] 变为 -1 。数组变为 [-3,-1,-1,2] 。
# 再选择索引 2 ，nums[2] 变为 0 。数组变为 [-3,-1,-1,0] 。
# 最后，数组的和为 (-3) + (-1) + (-1) + 0 = 2 。

# 提示：
# 1 <= nums.length <= 10^5
# -100 <= nums[i] <= 100
# 1 <= k <= nums.length


def largestSumAfterKNegations(nums, k):
    # 先将数组排序，将绝对值大的数字排在前面
    nums.sort(key=lambda x: abs(x), reverse=True)
    
    
    n = len(nums)
    # 将负数尽可能都变成正数
    for i in range(n):
        if nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            k -= 1
    
    # 将绝对值最小的数取反对总和影响最小
    if k % 2 == 1:
        nums[n-1] = -nums[n-1]
        
    return sum(nums)


if __name__ == '__main__':
    nums = [4,2,3]
    k = 1
    print(largestSumAfterKNegations(nums, k)) # 5

    nums = [3,-1,0,2]
    k = 3
    print(largestSumAfterKNegations(nums, k)) # 6
    
    nums = [2,-3,-1,5,-4]
    k = 2
    print(largestSumAfterKNegations(nums, k)) # 13
    