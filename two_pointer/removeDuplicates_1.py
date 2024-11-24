# 给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
# 元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
# 考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：
# 更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
# 返回 k 。

# 示例 1：
# 输入：nums = [1,1,2]
# 输出：2, nums = [1,2,_]
# 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
# 示例 2：
# 输入：nums = [0,0,1,1,1,2,2,3,3,4]
# 输出：5, nums = [0,1,2,3,4]
# 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。


# 双指针算法
def removeDuplicates(nums: list[int]) -> int:
    """定义两个指针 fast 和 slow 分别为快指针和慢指针，快指针表示遍历数组到达的下标位置，慢指针表示下一个不同元素要填入的下标位置，初始时两个指针都指向下标 1。
    假设数组 nums 的长度为 n。将快指针 fast 依次遍历从 1 到 n−1 的每个位置，对于每个位置，
    如果 nums[fast]=nums[fast−1]，说明 nums[fast] 和之前的元素都不同，因此将 nums[fast] 的值复制到 nums[slow]，然后将 slow 的值加 1，即指向下一个位置。
    遍历结束之后，从 nums[0] 到 nums[slow−1] 的每个元素都不相同且包含原数组中的每个不同的元素，因此新的长度即为 slow，返回 slow 即可。
    """
    if not nums:
        return 0

    n = len(nums)
    fast = slow = 1
    while fast < n:
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow


def removeDuplicates2(nums: list[int]) -> int:
    length = len(nums)
    if length == 0:
        return 0
    i = 0
    for j in range(1, length):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1


def removeDuplicates3(nums: list[int]) -> int:
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  # nums[i] 不是重复项
            nums[k] = nums[i]  # 保留 nums[i]
            k += 1
    return k


def removeDuplicates4(nums: list[int]) -> int:
    nums[:] = sorted(set(nums))  # 注：需要额外空间
    return len(nums)


if __name__ == "__main__":
    list_1 = removeDuplicates([1, 1, 1, 1, 1, 2, 2, 2, 3])
    list_2 = removeDuplicates([1, 1, 1, 2, 2])
    list_3 = removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3, 3])
    print(list_1, list_2, list_3)

    list_1 = removeDuplicates2([1, 1, 1, 1, 1, 2, 2, 2, 3])
    list_2 = removeDuplicates2([1, 1, 1, 2, 2])
    list_3 = removeDuplicates2([0, 0, 1, 1, 1, 1, 2, 3, 3, 3])
    print(list_1, list_2, list_3)
