# 题目：
# 给定一个整数数组int[] nums 和一个整数目标值 target，请你在该nums数组中找出 和为目标值 target  的2整数，并返回它们的数组下标。
# 每种输入必须会有一个答案，只需要返回一个正确的答案即可，数组中同一个元素在答案里不能重复出现，比如int[]=[3,2,4,6]  target=6，不可以返回[0,0]
# 可以以任意顺序返回
# 输入：nums = [2,7,11,15], target = 9     输出：[0,1]
# 输入：nums = [3,2,4,5], target = 6 输出[1,2]


def findTargetSum(nums, target):
    if len(nums) < 2:
        return [-1, -1]

    last_cur_map = dict()  # key: 当前数字,  values: 最早在数组中出现的index
    for i, num in enumerate(nums):
        if (t := target - num) in last_cur_map:  # 在last_cur查找是否有target-num
            return [last_cur_map[t], i]
        else:
            last_cur_map[num] = i
    return [-1, -1]


nums = [2, 7, 11, 15]
target = 9
print(findTargetSum(nums, target))

nums = [3, 2, 4, 5]
target = 6
print(findTargetSum(nums, target))

nums = [2, 2, 11, 15]
target = 4
print(findTargetSum(nums, target))

nums = [1, 2, 2, 11, 15]
target = 4
print(findTargetSum(nums, target))
