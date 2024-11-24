#
# * 统计特殊整数 - H
# 如果一个正整数每一个数位都是 互不相同 的，我们称它是特殊整数 。
# 给你一个 正 整数 n ，请你返回区间 [1, n] 之间特殊整数的数目。

# 示例 1：
# 输入：n = 20
# 输出：19
# 解释：1 到 20 之间所有整数除了 11 以外都是特殊整数。所以总共有 19 个特殊整数。
# 示例 2：
# 输入：n = 5
# 输出：5
# 解释：1 到 5 所有整数都是特殊整数。
# 示例 3：
# 输入：n = 135
# 输出：110
# 解释：从 1 到 135 总共有 110 个整数是特殊整数。
# 不特殊的部分数字为：22 ，114 和 131 。
from functools import cache


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        """空间复杂度：O(len(s)) = O(logn)
        对于dp问题 时间复杂度 = 状态个数 * 单一状态的执行时间
        O(len(s)) * 2^10 * 10 = O(logn) * 2^10 * 10  => O(logn) (log 是以10为底)"""

        # * 数位DP通用模版 v1.0
        s = str(n)

        # 返回从数字i开始填数字，i前面填的数字集合是mask，能构造出的特殊整数的数目
        # * i : 表示目前枚举到的下标位置
        # * mask : 表示目前选了那些数字的集合
        # * is_limit ：表示前面的数位有没有选择到该位的上限
        # 表示前面填的数字是否都和n对应位上的一致，如果为true，那么当前位之多填int(s[i])，否则至多为9
        # * is_num ：避免前导0的问题
        # 表示前面是否填了数字（是否跳过），如果为True，那么当前位可以从0开始，如果为False，那么我们可以跳过或者从1开始填数字

        @cache
        def dfs(i, mask, isLimit, isNum):
            if i == len(s):
                return 1 if isNum else 0
            res = 0
            # 当前位不填数字，前面必须也没填数字，isLimit一定是True
            if not isNum:
                res += dfs(i + 1, mask, False, False)

            # 当前位填数字，两种情况：前面没填数字，前面填了数字
            up = int(s[i]) if isLimit else 9
            low = 0 if isNum else 1
            for d in range(low, up + 1):
                if (mask >> d) & 1 == 0:  # d 没有使用过，所以可以使用 d
                    res += dfs(i + 1, mask | (1 << d), isLimit and d == up, True)
            return res

        return dfs(0, 0, True, False)


if __name__ == "__main__":
    s = Solution()
    n = 135
    print(s.countSpecialNumbers(n))
