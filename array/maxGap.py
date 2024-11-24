# 给定一个数组，求如果排序之后，相邻两数的最大差值。要求时间复杂度O(n),且要求不能用基于非比较的排序（计数排序，基数排序，桶排序）。
# 思路：将数组分成（n+1)个桶，桶与桶之间的最小差值一定大于桶内的最大差值。（设置了一个优良的平凡解，过滤掉很多不可能的答案）


def maxGap(nums):
    n = len(nums)
    if not nums or n < 2:
        return 0
    min_num = min(nums)
    max_num = max(nums)
    if max_num == min_num:
        return 0

    hasNum = [False] * (n + 1)
    maxs = [float("-inf")] * (n + 1)
    mins = [float("inf")] * (n + 1)

    for i in range(n):
        bucket_id = get_bucket_id(nums[i], n, min_num, max_num)
        # print(bucket_id)
        mins[bucket_id] = min(mins[bucket_id], nums[i])
        maxs[bucket_id] = max(maxs[bucket_id], nums[i])
        hasNum[bucket_id] = True
    # print(hasNum,maxs,mins)

    res = 0
    last_max = maxs[0]
    for i in range(1, n + 1):
        if hasNum[i]:
            res = max(res, mins[i] - last_max)
            last_max = maxs[i]
    return res


def get_bucket_id(num, n, min_num, max_num):
    return int((num - min_num) * (n) / (max_num - min_num))


if __name__ == "__main__":
    nums = [6, 3, 1, 7, 9]
    print(maxGap(nums))
