# 找出连续子数组的最大和

def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

# 贪心策略：
# 维护一个变量current_sum，初始值为nums[0]
# 遍历数组，对于每一个位置，计算当前位置的连续和
# 如果连续和小于0，则从当前位置重新开始计算
# 如果连续和大于0，则保留当前位置

def maxSubArray2(nums):
    start = 0
    end = 0
    result = float('-inf')
    count = 0
    for i in range(len(nums)):
        num = nums[i]
        count += num
        if count > result:
            result = count
            end = i
        if count < 0:       # 如果连续和小于0，则从当前位置重新开始计算
            count = 0
            start = i + 1
    return result, [start, end]     # 返回最大子数组的和和其起止位置[start, end](闭区间)
            


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))
    print(maxSubArray2(nums))