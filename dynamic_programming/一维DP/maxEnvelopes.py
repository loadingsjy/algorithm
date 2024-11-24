# * 354. 俄罗斯套娃信封问题 - H

# 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
# 当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
# 请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
# 注意：不允许旋转信封。

# 示例 1：
# 输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出：3
# 解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
# 示例 2：
# 输入：envelopes = [[1,1],[1,1],[1,1]]
# 输出：1

# 提示：
# 1 <= envelopes.length <= 105
# envelopes[i].length == 2
# 1 <= wi, hi <= 105


import bisect


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        """先按照 信封的宽度从小到大，如果宽度一样，高度由大到小 排序，然后求高度数组的最长递增子序列"""
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # ends[i] 表示长度为i+1的递增子序列中的末尾元素的最小值，ends数组一定严格递增，所以可以二分查找
        ends = []
        ans = 0
        for _, x in envelopes:
            j = bisect.bisect_left(ends, x)
            if j == len(ends):
                ends.append(x)
                ans += 1
            else:
                ends[j] = x
        return ans
