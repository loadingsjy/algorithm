import random


def partition(nums, left, right):
    # 随机从当前数组选取一个数作为分界线 randomly choose pivot
    random_num = nums[random.randint(left, right)]
    nums[left], random_num = random_num, nums[left]
    pivot = nums[left]

    i, j = left, right
    # 交换元素，使得分界线左边的元素都比分界线小，分界线右边的元素都比分界线大
    while i < j:
        while i < j and nums[j] >= pivot:
            j -= 1
        nums[i] = nums[j]

        while i < j and nums[i] < pivot:
            i += 1
        nums[j] = nums[i]

    # assert i == j
    nums[i] = pivot

    return i


# 快速排序
def quick_sort(nums, left, right):

    # left = 0
    # right = len(nums) - 1
    if left < right:
        mid = partition(nums, left, right)
        quick_sort(nums, left, mid - 1)
        quick_sort(nums, mid + 1, right)


if __name__ == "__main__":
    nums = [6, 2, 8, 3, 1, 5, 10]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
