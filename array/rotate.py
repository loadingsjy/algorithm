# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

# 示例 1:

# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]

def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]


# Test
a = [1, 2, 3, 4, 5, 6, 7]
b = [3, 99, -1, -100]
rotate(a, 3)
rotate(b, 2)
print(a)   # [5,6,7,1,2,3,4]
print(b)   # [-1,-100,3,99]
