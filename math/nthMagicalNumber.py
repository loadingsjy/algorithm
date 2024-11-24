#
# * 878. 第 N 个神奇数字

# 一个正整数如果能被 a 或 b 整除，那么它是神奇的。
# 给定三个整数 n , a , b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案 对 109 + 7 取模 后的值。

# 示例 1：
# 输入：n = 1, a = 2, b = 3
# 输出：2
# 示例 2：
# 输入：n = 4, a = 2, b = 3
# 输出：6
import math
from bisect import bisect_left


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # def gcd(a, b):
        #     """求a与b的最大公约数，时间复杂度O((loga)^3)"""
        #     return a if b == 0 else gcd(b, a % b)

        # def lcm(a, b):
        #     """求a与b的最小公倍数"""
        #     return a // gcd(a, b) * b

        lcm_ab = math.lcm(a, b)
        left = 0
        right = min(a, b) * n
        while left <= right:
            mid = (left + right) // 2
            if mid // a + mid // b - mid // lcm_ab >= n:
                right = mid - 1
            else:
                left = mid + 1
        return left % (10**9 + 7)

    def nthMagicalNumber2(self, n: int, a: int, b: int) -> int:
        """灵神写法"""
        lcm = math.lcm(a, b)
        left, right = 0, min(a, b) * n  # 开区间 (left, right)
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            if mid // a + mid // b - mid // lcm >= n:
                right = mid  # 范围缩小到 (left, mid)
            else:
                left = mid  # 范围缩小到 (mid, right)
        return right % (10**9 + 7)

    def nthMagicalNumber3(self, n: int, a: int, b: int) -> int:
        """使用库函数二分（Python 3.10 支持通过 key 自定义二分规则）"""
        lcm = math.lcm(a, b)
        return bisect_left(
            range(min(a, b) * n), n, key=lambda x: x // a + x // b - x // lcm
        ) % (10**9 + 7)


if __name__ == "__main__":
    s = Solution()
    a, b, n = 3, 7, 1000
    print(s.nthMagicalNumber(n, a, b))
    print(s.nthMagicalNumber2(n, a, b))
    print(s.nthMagicalNumber3(n, a, b))
