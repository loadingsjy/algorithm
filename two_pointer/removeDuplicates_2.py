# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


def removeDuplicates_my(nums: list[int]) -> int:
    length = len(nums)
    if length <= 2:
        return length
    t = 0
    i = t + 2

    while i < length:
        if nums[i] == nums[t]:
            del nums[i]
            length -= 1
        else:
            t += 1
            i = t + 2

    # print(nums)
    return len(nums)


# 双指针法
def removeDuplicates_improved(nums: list[int]) -> int:
    n = len(nums)
    if n <= 2:
        return n
    # slow, fast = 2, 2
    # while fast < n:
    #     if nums[slow - 2] != nums[fast]:
    #         nums[slow] = nums[fast]
    #         slow += 1
    #     fast += 1
    # print(nums)
    # return slow

    i = 2
    for j in range(2, n):
        if nums[i - 2] != nums[j]:
            nums[i] = nums[j]
            i += 1
    # print(nums)
    return i


def removeDuplicates2(nums: list[int]) -> int:
    def solve(k, nums):  # 只保留k个相同元素的通用写法
        n = len(nums)
        i = k
        for j in range(k, n):
            if nums[i - k] != nums[j]:
                nums[i] = nums[j]
                i += 1
        return i

    return solve(2, nums)


def removeDuplicates3(nums: list[int]) -> int:
    def solve(k):  # 只保留k个相同元素的通用写法
        u = 0
        for x in nums:
            if u < k or nums[u - k] != x:
                nums[u] = x
                u += 1
        return u

    return solve(2)


if __name__ == "__main__":
    nums1 = [1, 1, 1, 1, 1, 2, 2, 2, 3]
    nums2 = [1, 1, 1, 2, 2, 3]
    nums3 = [0, 0, 1, 1, 1, 1, 2, 3, 3, 3]

    n_1 = removeDuplicates_my([1, 1, 1, 1, 1, 2, 2, 2, 3])
    n_1_ = removeDuplicates_improved([1, 1, 1, 1, 1, 2, 2, 2, 3])
    n_1_2 = removeDuplicates2([1, 1, 1, 1, 1, 2, 2, 2, 3])
    n_1_3 = removeDuplicates3([1, 1, 1, 1, 1, 2, 2, 2, 3])

    n_2 = removeDuplicates_my([1, 1, 1, 2, 2, 3])
    n_2_ = removeDuplicates_improved([1, 1, 1, 2, 2, 3])
    n_2_2 = removeDuplicates2([1, 1, 1, 2, 2, 3])
    n_2_3 = removeDuplicates3([1, 1, 1, 2, 2, 3])

    n_3 = removeDuplicates_my([0, 0, 1, 1, 1, 1, 2, 3, 3, 3])
    n_3_ = removeDuplicates_improved([0, 0, 1, 1, 1, 1, 2, 3, 3, 3])
    n_3_2 = removeDuplicates2([0, 0, 1, 1, 1, 1, 2, 3, 3, 3])
    n_3_3 = removeDuplicates3([0, 0, 1, 1, 1, 1, 2, 3, 3, 3])

    print(n_1, n_2, n_3)
    print(n_1_, n_2_, n_3_)
    print(n_1_2, n_2_2, n_3_2)
    print(n_1_3, n_2_3, n_3_3)
