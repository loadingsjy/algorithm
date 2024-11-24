#
# * 2848. 与车相交的点 - E
# 给你一个下标从 0 开始的二维整数数组 nums 表示汽车停放在数轴上的坐标。对于任意下标 i，nums[i] = [starti, endi] ，
# 其中 starti 是第 i 辆车的起点，endi 是第 i 辆车的终点。
# 返回数轴上被车 任意部分 覆盖的整数点的数目。

# 示例 1：
# 输入：nums = [[3,6],[1,5],[4,7]]
# 输出：7
# 解释：从 1 到 7 的所有点都至少与一辆车相交，因此答案为 7 。
# 示例 2：
# 输入：nums = [[1,3],[5,8]]
# 输出：7
# 解释：1、2、3、5、6、7、8 共计 7 个点满足至少与一辆车相交，因此答案为 7 。

# 提示：
# 1 <= nums.length <= 100
# nums[i].length == 2
# 1 <= starti <= endi <= 100


from itertools import accumulate


class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        """模拟 差分数组 合并区间 哈希表"""
        max_num = max(nums, key=lambda x: x[1])[1]
        diff = [0] * (max_num + 2)
        for s, e in nums:
            diff[s] += 1
            diff[e + 1] -= 1
        ans = 0
        for i in range(1, max_num + 2):
            diff[i] += diff[i - 1]
            if diff[i] != 0:
                ans += 1
        return ans

    def numberOfPoints2(self, nums: list[list[int]]) -> int:
        """灵神写法"""
        max_end = max(end for _, end in nums)
        diff = [0] * (max_end + 2)  # 注意下面有 end+1
        for start, end in nums:
            diff[start] += 1
            diff[end + 1] -= 1
        return sum(s > 0 for s in accumulate(diff))


if __name__ == "__main__":
    sol = Solution()
    nums = [[3, 6], [1, 5], [4, 7]]
    print(sol.numberOfPoints(nums))
    print(sol.numberOfPoints2(nums))
