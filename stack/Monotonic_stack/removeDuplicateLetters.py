#
# * 316. 去除重复字母 - M
# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
# 最小（要求不能打乱其他字符的相对位置）。

# 示例 1：
# 输入：s = "bcabc"
# 输出："abc"
# 示例 2：
# 输入：s = "cbacdcbc"
# 输出："acdb"
# 提示：
# 1 <= s.length <= 10^4
# s 由小写英文字母组成

from collections import Counter


class Solution:

    def removeDuplicateLetters(self, s: str) -> str:

        # key:字符，value:剩余可使用数量，如果为0代表没有可以使用的
        rest = Counter(s)
        used = set()  # stack 里面已经有的字符
        stack = []
        for ch in s:
            rest[ch] -= 1
            if ch in used:  # 前面有了，且你的位置还在他的后面
                continue
            while stack and ch < stack[-1] and rest[stack[-1]] > 0:
                # rest[stack[-1]] > 0 代表stack[-1]剩余还可用，所以可以pop
                used.remove(stack.pop())
            stack.append(ch)
            used.add(ch)

        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()
    s = "cbacdcbc"
    print(sol.removeDuplicateLetters(s))
