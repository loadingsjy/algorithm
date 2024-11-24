# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
# 示例 1：
# 输入：x = 4
# 输出：2
# 示例 2：
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        """牛顿迭代法"""

        def newton(i, x):
            res = (i + x / i) / 2.0
            while abs(res - i) > 1e-5:
                i = res
                res = (i + x / i) / 2.0
            return res

        if x == 0:
            return 0
        return int(newton(x, x))

    def mySqrt2(self, x: int) -> int:
        """用指数函数 exp 和对数函数 ln 代替平方根函数"""
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans

    def mySqrt3(self, x: int) -> int:
        """二分查找法"""
        if x == 0 or x == 1:
            return x
        left = 0.0
        if 0 < x < 1:
            right = 1.0
        elif x > 1:
            right = float(x)

        while abs(right - left) > 1e-5:
            mid = (left + right) / 2.0
            if mid * mid - x == 0:
                return int(mid)
            elif mid * mid > x:
                right = mid
            else:
                left = mid
        ans = int(mid)
        return ans + 1 if (ans + 1) * (ans + 1) == x else ans


if __name__ == "__main__":
    s = Solution()
    num = 100
    print(s.mySqrt(num))
    print(s.mySqrt2(num))
    print(s.mySqrt3(num))
