#
# * 646. 最长数对链 - M

# 给你一个由 n 个数对组成的数对数组 pairs ，其中 pairs[i] = [lefti, righti] 且 lefti < righti 。
# 现在，我们定义一种 跟随 关系，当且仅当 b < c 时，数对 p2 = [c, d] 才可以跟在 p1 = [a, b] 后面。我们用这种形式来构造 数对链 。
# 找出并返回能够形成的 最长数对链的长度 。
# 你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。

# 示例 1：
# 输入：pairs = [[1,2], [2,3], [3,4]]
# 输出：2
# 解释：最长的数对链是 [1,2] -> [3,4] 。
# 示例 2：
# 输入：pairs = [[1,2],[7,8],[4,5]]
# 输出：3
# 解释：最长的数对链是 [1,2] -> [4,5] -> [7,8] 。

# 提示：
# n == pairs.length
# 1 <= n <= 1000
# -1000 <= lefti < righti <= 1000


import bisect
from math import inf


class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        """动态规划:
        定义 dp[i] 为以 pairs[i] 为结尾的最长数对链的长度。
        计算 dp[i] 时，可以先找出所有的满足 pairs[i][0]>pairs[j][1] 的 j，并求出最大的 dp[j]，dp[i] 的值即可赋为这个最大值加一。
        这种动态规划的思路要求计算 dp[i] 时，所有潜在的 dp[j] 已经计算完成，可以先将 pairs 进行排序来满足这一要求。初始化时，dp 需要全部赋值为 1。
        """
        pairs.sort()
        dp = [1] * len(pairs)
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]

    def findLongestChain2(self, pairs: list[list[int]]) -> int:
        """最长递增子序列"""
        pairs.sort(key=lambda x: x[0])
        # ends[i] 表示长度为i+1的递增子序列中的末尾元素[1]的最小值
        ends = []
        ans = 0
        for x, y in pairs:
            j = bisect.bisect_left(ends, x)  # 用前一个数字进行查找
            if j == len(ends):
                ends.append(y)
                ans += 1
            else:
                # end数组放的的后一个数组的最小值
                ends[j] = min(ends[j], y)
        return ans

    def findLongestChain3(self, pairs: list[list[int]]) -> int:
        """贪心: 先根据结尾位置进行排序，在每次看后一个的x(cur) 是否大于前一个y（prev）就加入答案，把pre设置成cur，继续重复操作
        类似于 最多会议安排 -> 最早结束的会议最先安排
        要挑选最长数对链的第一个数对时，最优的选择是挑选第二个数字最小的，这样能给挑选后续的数对留下更多的空间。
        挑完第一个数对后，要挑第二个数对时，也是按照相同的思路，是在剩下的数对中，第一个数字满足题意的条件下，挑选第二个数字最小的。
        按照这样的思路，可以先将输入按照第二个数字排序，然后不停地判断第一个数字是否能满足大于前一个数对的第二个数字即可。
        """
        cur, res = -inf, 0
        for x, y in sorted(pairs, key=lambda p: p[1]):
            if cur < x:
                cur = y
                res += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    pairs = [[1, 2], [2, 3], [3, 4]]
    print(sol.findLongestChain(pairs))
    print(sol.findLongestChain2(pairs))
    print(sol.findLongestChain3(pairs))
