#
# * 3261. 统计满足 K 约束的子字符串数量 II - H
# 给你一个 二进制 字符串 s 和一个整数 k。
# 另给你一个二维整数数组 queries ，其中 queries[i] = [li, ri] 。
# 如果一个 二进制字符串 满足以下任一条件，则认为该字符串满足 k 约束：
# ·字符串中 0 的数量最多为 k。
# ·字符串中 1 的数量最多为 k。
# 返回一个整数数组 answer ，其中 answer[i] 表示 s[li..ri] 中满足 k 约束 的 子字符串的数量。
# 示例 1：
# 输入：s = "0001111", k = 2, queries = [[0,6]]
# 输出：[26]
# 解释：
# 对于查询 [0, 6]， s[0..6] = "0001111" 的所有子字符串中，除 s[0..5] = "000111" 和 s[0..6] = "0001111" 外，其余子字符串都满足 k 约束。
# 示例 2：
# 输入：s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]]
# 输出：[15,9,3]
# 解释：
# s 的所有子字符串中，长度大于 3 的子字符串都不满足 k 约束。
# 提示：
# 1 <= s.length <= 105
# s[i] 是 '0' 或 '1'
# 1 <= k <= s.length
# 1 <= queries.length <= 105
# queries[i] == [li, ri]
# 0 <= li <= ri < s.length
# 所有查询互不相同

from typing import List
from bisect import bisect_left


class Solution:
    def countKConstraintSubstrings(
        self, s: str, k: int, queries: List[List[int]]
    ) -> List[int]:
        """滑动窗口 + 前缀和 + 二分查找"""
        n = len(s)
        cnt = [0, 0]
        left = [0] * n
        pre_ans = [0] * (n + 1)     # pre_ans[i]代表所有以s[i]为结尾的满足题意的子串的个数

        l = 0
        for r, ch in enumerate(s):
            cnt[int(ch)] += 1
            while cnt[0] > k and cnt[1] > k:
                cnt[int(s[l])] -= 1
                l += 1
            left[r] = l
            # 计算s[0:r+1]的所有符合条件的子串的个数
            pre_ans[r + 1] = pre_ans[r] + r - l + 1

        ans = []
        for l, r in queries:
            j = bisect_left(left, l, l, r + 1)
            ans.append(pre_ans[r + 1] - pre_ans[j] + (j - l + 1) * (j - l) // 2)
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "010101"
    k = 1
    queries = [[0, 5], [1, 4], [2, 3]]
    print(sol.countKConstraintSubstrings(s, k, queries))
