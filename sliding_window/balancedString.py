#
# * 1234. 替换子串得到平衡字符串 - H
# 有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。
# 假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。
# 给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。
# 你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。
# 请返回待替换子串的最小可能长度。
# 如果原字符串自身就是一个平衡字符串，则返回 0。

# 示例 1：
# 输入：s = "QWER"
# 输出：0
# 解释：s 已经是平衡的了。
# 示例 2：
# 输入：s = "QQWE"
# 输出：1
# 解释：我们需要把一个 'Q' 替换成 'R'，这样得到的 "RQWE" (或 "QRWE") 是平衡的。
# 示例 3：
# 输入：s = "QQQW"
# 输出：2
# 解释：我们可以把前面的 "QQ" 替换成 "ER"。
# 示例 4：
# 输入：s = "QQQQ"
# 输出：3
# 解释：我们可以替换后 3 个 'Q'，使 s = "QWER"。

# 提示：
# 1 <= s.length <= 10^5
# s.length 是 4 的倍数
# s 中只含有 'Q', 'W', 'E', 'R' 四种字符


class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        if n % 4 != 0:
            return -1

        require = n // 4  # 每种字符需要的数量
        CHAR_MAPPING = {"Q": 0, "W": 1, "E": 2, "R": 3}
        cnt = [0] * 4
        for ch in s:
            cnt[CHAR_MAPPING[ch]] += 1

        def check(cnt, length):
            """
            cnt：剩余字符构成的子串表，
            length: 当前窗口的长度，
            返回当前对窗口进行调整，能否是全局字符满足平衡字符串
            """
            for i in range(len(cnt)):
                if cnt[i] > require:
                    return False
                length -= require - cnt[i]
            return length == 0

        ans = n

        right = -1
        for left, ch in enumerate(s):
            while not check(cnt, right - left + 1) and right + 1 < n:
                cnt[CHAR_MAPPING[s[right + 1]]] -= 1
                right += 1
            # 跳出while循环后，有两种可能：
            # 1）可以对窗口内的字符进行调整满足全局是平衡字符串
            # 2）窗口右边界到了最后，窗口内字符串也不满足待替换子串
            if check(cnt, right - left + 1):
                ans = min(ans, right - left + 1)
            else:  # 窗口右边界到了最后，窗口内字符串也不满足待替换子串，则后面就没有答案了
                break
            cnt[CHAR_MAPPING[ch]] += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "QQQW"
    print(sol.balancedString(s))
