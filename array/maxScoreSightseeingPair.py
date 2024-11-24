#
# * 1014. 最佳观光组合 - M
# 给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。
# 一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离。
# 返回一对观光景点能取得的最高分。

# 示例 1：
# 输入：values = [8,1,5,2,6]
# 输出：11
# 解释：i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
# 示例 2：
# 输入：values = [1,2]
# 输出：2

# 提示：
# 2 <= values.length <= 5 * 104
# 1 <= values[i] <= 1000


class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        n = len(values)
        """枚举右，维护左的最大值：
        我们可以将得分公式拆分成 values[i]+i 和 values[j]−j 两部分，这样对于统计景点 j 答案的时候，由于 values[j]−j 是固定不变的，
        因此最大化 values[i]+i+values[j]−j 的值其实就等价于求 [0,j−1] 中 values[i]+i 的最大值 mx，景点 j 的答案即为 pre_max+values[j]−j 。"""
        pre_max = values[0]
        ans = float("-inf")
        for i in range(1, n):
            ans = max(ans, pre_max + values[i] - i)
            pre_max = max(pre_max, i + values[i])
        return ans


if __name__ == "__main__":
    sol = Solution()
    values = [8, 1, 5, 2, 6]
    print(sol.maxScoreSightseeingPair(values))
