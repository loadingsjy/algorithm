#
# * 1124. 表现良好的最长时间段

# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
# 请你返回「表现良好时间段」的最大长度。

# 示例 1：
# 输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。
# 示例 2：
# 输入：hours = [6,6,6]
# 输出：0


class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        mp = dict()
        mp[0] = -1
        pre_sum = 0
        ans = 0

        for i, hour in enumerate(hours):
            pre_sum += 1 if hour > 8 else -1
            if pre_sum > 0:
                ans = max(ans, i + 1)
            else:
                if (pre_sum - 1) in mp:
                    ans = max(ans, i - mp[pre_sum - 1])
                if pre_sum not in mp:
                    mp[pre_sum] = i
        return ans


if __name__ == "__main__":
    s = Solution()
    hours = [9, 9, 6, 0, 6, 6, 9]
    print(s.longestWPI(hours))
