# 3258. 统计满足 K 约束的子字符串数量 I - E
# 给你一个 二进制 字符串 s 和一个整数 k。
# 如果一个 二进制字符串 满足以下任一条件，则认为该字符串满足 k 约束：
# · 字符串中 0 的数量最多为 k。
# · 字符串中 1 的数量最多为 k。
# 返回一个整数，表示 s 的所有满足 k 约束 的子字符串的数量。
# 示例 1：
# 输入：s = "10101", k = 1
# 输出：12
# 解释：
# s 的所有子字符串中，除了 "1010"、"10101" 和 "0101" 外，其余子字符串都满足 k 约束。
# 示例 2：
# 输入：s = "1010101", k = 2
# 输出：25
# 解释：
# s 的所有子字符串中，除了长度大于 5 的子字符串外，其余子字符串都满足 k 约束。
# 示例 3：
# 输入：s = "11111", k = 1
# 输出：15
# 解释：
# s 的所有子字符串都满足 k 约束。

# 提示：
# 1 <= s.length <= 50
# 1 <= k <= s.length
# s[i] 是 '0' 或 '1'。


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        one_cnt, zero_cnt = 0, 0
        n = len(s)
        left = 0
        ans = 0
        for right in range(n):
            if s[right] == "0":
                zero_cnt += 1
            else:
                one_cnt += 1

            while left <= right and one_cnt > k and zero_cnt > k:
                if s[left] == "0":
                    zero_cnt -= 1
                else:
                    one_cnt -= 1
                left += 1

            ans += right - left + 1
        return ans

    def countKConstraintSubstrings2(self, s: str, k: int) -> int:
        """灵神写法"""
        ans = left = 0
        cnt = [0, 0]
        for i, c in enumerate(s):
            cnt[ord(c) & 1] += 1
            while cnt[0] > k and cnt[1] > k:
                cnt[ord(s[left]) & 1] -= 1
                left += 1
            ans += i - left + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "1010101"
    k = 2
    print(sol.countKConstraintSubstrings(s, k))
    print(sol.countKConstraintSubstrings2(s, k))