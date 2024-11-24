def merge_sort_re(nums):
    """归并排序：递归版"""
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        merge_sort_re(left)
        merge_sort_re(right)

        l1, l2 = len(left), len(right)
        i, j, k = 0, 0, 0
        while i < l1 and j < l2:
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < l1:
            nums[k] = left[i]
            i += 1
            k += 1
        while j < l2:
            nums[k] = right[j]
            j += 1
            k += 1
    return nums


def merge(left, right):
    l1, l2 = len(left), len(right)
    nums = [0] * (l1 + l2)
    i, j, k = 0, 0, 0
    while i < l1 and j < l2:
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    while i < l1:
        nums[k] = left[i]
        i += 1
        k += 1
    while j < l2:
        nums[k] = right[j]
        j += 1
        k += 1
    return nums


def merge_sort_iter(arr):
    """归并排序：非递归版"""
    n = len(nums)
    step = 1
    while step < n:
        l = 0
        while l < n:
            mid = l + step - 1
            if mid + 1 >= n:  # 没有右侧部分
                break
            r = min(n - 1, l + step * 2 - 1)
            nums[l : r + 1] = merge(nums[l : mid + 1], nums[mid + 1 : r + 1])
            l = r + 1
        step <<= 1
    return nums


if __name__ == "__main__":
    nums = [5, 1, 1, 2, 0, 0]
    print(merge_sort_re(nums))
    print(merge_sort_iter(nums))
