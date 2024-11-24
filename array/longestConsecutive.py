# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

# 示例 1：

# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 示例 2：

# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9


def get_max_length(n, nums_set):
    max_length = 1
    while n + 1 in nums_set:
        max_length += 1
        n += 1
    return max_length


def longestConsecutive(nums: list[int]) -> int:
    max_l = 1
    nums_set = set(nums)
    for n in list(nums_set):
        # 以 n - 1 为开头的连续序列长度一定大于以n为开头的连续序列长度，所以跳过
        if n - 1 not in nums_set:
            max_l = max(get_max_length(n, nums_set), max_l)

    return max_l


def longestConsecutive2(nums):
    """题目要求 O(n) 复杂度。
    用哈希表存储每个端点值对应连续区间的长度
    若数已在哈希表中：跳过不做处理
    若是新数加入：
        1.取出其左右相邻数已有的连续区间长度 left 和 right
        2.计算当前数的区间长度为：cur_length = left + right + 1
        3.根据 cur_length 更新最大长度 max_length 的值
        4.更新区间两端点的长度值"""
    hash_dict = dict()

    max_length = 0
    for num in nums:
        if num not in hash_dict:
            left = hash_dict.get(num - 1, 0)
            right = hash_dict.get(num + 1, 0)

            cur_length = 1 + left + right
            if cur_length > max_length:
                max_length = cur_length

            hash_dict[num] = cur_length
            hash_dict[num - left] = cur_length
            hash_dict[num + right] = cur_length

    return max_length


if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(nums))
    print(longestConsecutive2(nums))

    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(longestConsecutive(nums))
    print(longestConsecutive2(nums))
