#
# * 1590. 使数组和能被 P 整除

# 给你一个正整数数组 nums，请你移除 最短 子数组（可以为 空），使得剩余元素的 和 能被 p 整除。 不允许 将整个数组都移除。
# 请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 -1 。
# 子数组 定义为原数组中连续的一组元素。


# 示例 1：
# 输入：nums = [3,1,4,2], p = 6
# 输出：1
# 解释：nums 中元素和为 10，不能被 p 整除。我们可以移除子数组 [4] ，剩余元素的和为 6 。
# 示例 2：
# 输入：nums = [6,3,5,2], p = 9
# 输出：2
# 解释：我们无法移除任何一个元素使得和被 9 整除，最优方案是移除子数组 [5,2] ，剩余元素为 [6,3]，和为 9 。
# 示例 3：
# 输入：nums = [1,2,3], p = 3
# 输出：0
# 解释：和恰好为 6 ，已经能被 3 整除了。所以我们不需要移除任何元素。
# 示例  4：
# 输入：nums = [1,2,3], p = 7
# 输出：-1
# 解释：没有任何方案使得移除子数组后剩余元素的和被 7 整除。
# 示例 5：
# 输入：nums = [1000000000,1000000000,1000000000], p = 3
# 输出：0


class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        mod = sum(nums) % p  # 整体余数
        if mod == 0:
            return 0
        n = len(nums)
        mp = dict()
        mp[0] = -1
        cur_mod = 0
        ans = n
        for i, num in enumerate(nums):
            cur_mod = (cur_mod + num) % p  # 当前0..i的子数组和的余数
            find = (cur_mod + p - mod) % p
            if find in mp:
                ans = min(ans, i - mp[find])
            mp[cur_mod] = i  # 记录当前前缀余数最晚出现的位置

        return -1 if ans == n else ans


if __name__ == "__main__":
    s = Solution()
    nums = [3, 1, 4, 2]
    p = 6
    print(s.minSubarray(nums, p))

    nums = [6, 3, 5, 2]
    p = 9
    print(s.minSubarray(nums, p))
