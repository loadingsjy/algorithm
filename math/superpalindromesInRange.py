#
# * 906. 超级回文数

# 如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。
# 现在，给定两个正整数 L 和 R （以字符串形式表示），返回包含在范围 [L, R] 中的超级回文数的数目。

# 示例：
# 输入：L = "4", R = "1000"
# 输出：4
# 解释：
# 4，9，121，以及 484 是超级回文数。
# 注意 676 不是一个超级回文数： 26 * 26 = 676，但是 26 不是回文数。

# 提示：
# 1 <= len(L) <= 18
# 1 <= len(R) <= 18
# L 和 R 是表示 [1, 10^18) 范围的整数的字符串。
# int(L) <= int(R)
import math


# 另外一种思路，打表法，10^18以内只有86个满足条件的回文数，列出来，放到数组里，然后根据L和R得出结果
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:

        def Enlarge(seed, even=True):
            """将num扩展成回文数，even代表生成偶数长度的回文数"""
            ans = seed
            if not even:
                seed //= 10
            while seed:
                ans = ans * 10 + seed % 10
                seed //= 10
            return ans

        def isPalindrome(num):
            offset = 1
            while num // offset >= 10:
                offset *= 10
            while num:
                if num // offset != num % 10:
                    return False
                num = (num % offset) // 10
                offset //= 100
            return True

        def isPalindrome2(x: int) -> bool:
            if num < 0 or (num % 10 == 0 and num != 0):
                return False
            reversed_num = 0
            while num > reversed_num:
                reversed_num = reversed_num * 10 + num % 10
                num //= 10
            return num == reversed_num or num == reversed_num // 10

        def check(ans, l, r):
            return ans >= l and ans <= r and isPalindrome2(ans)

        left = int(left)
        right = int(right)
        limit = int(math.sqrt(right))
        seed = 1  # 枚举量
        num = 0  # 根号x
        count = 0  # 计数
        while num < limit:  # 用小的那个回文数判断
            """先生成基于seed的回文数（两种长度），再判断num*num是不是回文数"""
            num = Enlarge(seed, True)
            if check(num * num, left, right):
                count += 1
            num = Enlarge(seed, False)
            if check(num * num, left, right):
                count += 1
            seed += 1
        return count
