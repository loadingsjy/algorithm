# 输入int型数组，询问该数组能否分成两组，使得两组中各元素加起来的和相等，并且，
# 所有5的倍数必须在其中一个组中，所有3的倍数在另一个组中（不包括5的倍数），不是5的倍数也不是3的倍数能放在任意一组，可以将数组分为空数组，
# 能满足以上条件，输出true；不满足时输出false。

# 数据范围：每个数组大小满足 1≤n≤50
# 输入的数据大小满足 ∣val∣≤500
# 输入描述：
# 第一行是数据个数，第二行是输入的数据
# 输出描述：
# 返回true或者false
# 示例1
# 输入：
# 4
# 1 5 -5 1
# 输出：
# true
# 说明：
# 第一组：5 -5 1
# 第二组：1


from functools import cache

def canPartition(nums):
    sum_5 = 0
    sum_3 = 0
    sum_other = 0
    other = []
    for n in nums:
        if n % 5 == 0:
            sum_5 += n
        elif n % 3 == 0 and n % 5 != 0:
            sum_3 += n
        else:
            other.append(n)
            sum_other += n

    if not other:
        return sum_3 == sum_5

    x, div = divmod(sum_other + sum_3 - sum_5, 2)  # 计算两个数组剩下需要多少数字和，x为剩下数字需要加到被5整除那组的数字和
    if div == 1 or len(other) < 2:  # 不能整除或者剩下只有一个数不能正好分组
        return False

    # y = sum_other - x

    # 从other选出一些数(有正有负有零），正好等于t（可正可负可零），是否可行
    @cache
    def dfs(index, t):

        if t == 0:
            return True
        if index == len(other):
            return False
        return dfs(index + 1, t) or dfs(index + 1 , t - other[index])
    return dfs(0, x)


if __name__ == "__main__":
    nums = [1, 5, -5, 1]
    print(canPartition(nums))

    nums = [3, 5, 496]
    print(canPartition(nums))

    nums = [3, 5, -1, -7]
    print(canPartition(nums))
