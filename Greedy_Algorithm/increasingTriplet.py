# 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
# 如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。


# 示例 1：
# 输入：nums = [1,2,3,4,5]
# 输出：true
# 解释：任何 i < j < k 的三元组都满足题意

# 示例 2：
# 输入：nums = [5,4,3,2,1]
# 输出：false
# 解释：不存在满足题意的三元组

# 示例 3：
# 输入：nums = [2,1,5,0,4,6]
# 输出：true
# 解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6


# 暴力搜索
def increasingTriplet(nums: list[int]) -> bool:
    i = 0
    while i < len(nums)-2:
        for j in range(i+1, len(nums)-1):
            if nums[i] < nums[j]:
                for k in range(j+1, len(nums)):
                    if nums[j] < nums[k]:
                        return True
        i += 1
    return False


# 找到数组中比n大的第一个元素的索引
def find_frist_index(nums, n):
    if max(nums) <= n:
        return -1
    index = -1
    for j in range(0, len(nums)):
        if nums[j] > n:
            index = j
            break
    return index


def increasingTriplet_v2(nums: list[int]) -> bool:
    n = len(nums)
    if n < 3:
        return False
    i = 0
    j = i + 1
    negative_frist_indexs = set()
    
    while i < n-2:
        if i in negative_frist_indexs or j >= n - 1:
            i += 1
            j = i+1
            continue

        if nums[j] <= nums[i]:
            j += 1
            continue
        
        if find_frist_index(nums[j+1:], nums[j]) != -1:
            return True
        else:
            negative_frist_indexs.add(j)
            j += 1
    
    return False


def increasingTriplet_v3(nums: list[int]) -> bool:
    n = len(nums)
    if n < 3:
        return False
    leftMin = [0] * n
    leftMin[0] = nums[0]
    for i in range(1, n):
        leftMin[i] = min(leftMin[i - 1], nums[i])
    rightMax = [0] * n
    rightMax[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], nums[i])
    for i in range(1, n - 1):
        if leftMin[i - 1] < nums[i] < rightMax[i + 1]:
            return True
    return False
            
        


if __name__ == '__main__':    
    nums = [1,2,3,4,5]
    print(increasingTriplet(nums)) # True
    print(increasingTriplet_v2(nums)) # True
    print(increasingTriplet_v3(nums)) # True
    print()

    nums = [5,4,3,2,1]
    print(increasingTriplet(nums)) # False
    print(increasingTriplet_v2(nums)) # False
    print(increasingTriplet_v3(nums)) # False
    print()

    nums = [2,1,5,0,4,6]
    print(increasingTriplet(nums)) # True
    print(increasingTriplet_v2(nums)) # True
    print(increasingTriplet_v3(nums)) # True
    print()
    
    nums = [20,100,10,12,5,13]
    print(increasingTriplet(nums)) # True
    print(increasingTriplet_v2(nums)) # True
    print(increasingTriplet_v3(nums)) # True
    print()
    

    nums = [1,5,0,4,1,3]
    print(increasingTriplet(nums)) # True
    print(increasingTriplet_v2(nums)) # True
    print(increasingTriplet_v3(nums)) # True
    print()



        
    