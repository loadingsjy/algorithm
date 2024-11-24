# 给定两个字符串, s 和 goal。如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true 。
# s 的 旋转操作 就是将 s 最左边的字符移动到最右边。 

# 例如, 若 s = 'abcde'，在旋转一次之后结果就是'bcdea' 。
# 示例 1:
# 输入: s = "abcde", goal = "cdeab"
# 输出: true
# 示例 2:
# 输入: s = "abcde", goal = "abced"
# 输出: false


# 思路：将s复制两份并拼接得到s'，如果goal是s'的子串，则返回true。

from kmp import kmp, kmp_v2
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s1 = s + s
        res = kmp(goal, s1)
        # res1 = kmp_v2(goal, s1)
        # assert res == res1
        if res:
            return True
        else:
            return False
        
        
if __name__ == '__main__':
    s = "abcde"
    goal = "cdeab"
    print(Solution().rotateString(s, goal))