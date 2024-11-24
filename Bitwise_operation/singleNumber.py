#
# * 260. 只出现一次的数字 III - H

# 给你一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
# 你必须设计并实现线性时间复杂度的算法且仅使用常量额外空间来解决此问题。

# 示例 1：
# 输入：nums = [1,2,1,3,2,5]
# 输出：[3,5]
# 解释：[5, 3] 也是有效的答案。
# 示例 2：
# 输入：nums = [-1,0]
# 输出：[-1,0]
# 示例 3：
# 输入：nums = [0,1]
# 输出：[1,0]


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xorsum = 0
        for num in nums:
            xorsum ^= num

        # lsb = xorsum & (~xorsum + 1)  # Brain Kernighan算法：提取xorsum最右边的1
        lsb = xorsum & (-xorsum)  # 两种写法都可以，因为 ~xorsum + 1 == -xorsum
        res1 = res2 = 0
        for num in nums:
            if num & lsb:
                res1 ^= num
            # else:
            #     res2 ^= num

        return [res1, xorsum ^ res1]


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 1, 3, 2, 5]
    print(s.singleNumber(nums))
