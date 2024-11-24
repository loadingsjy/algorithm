#
# * 29. 两数相除 - M

# 给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求 不使用 乘法、除法和取余运算。
# 整数除法应该向零截断，也就是截去（truncate）其小数部分。例如，8.345 将被截断为 8 ，-2.7335 将被截断至 -2 。
# 返回被除数 dividend 除以除数 divisor 得到的 商 。
# 注意：假设我们的环境只能存储 32 位 有符号整数，其数值范围是 [−231,  231 − 1] 。本题中，如果商 严格大于 231 − 1 ，则返回 231 − 1 ；如果商 严格小于 -231 ，则返回 -231 。

# 示例 1:
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = 3.33333.. ，向零截断后得到 3 。
# 示例 2:
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = -2.33333.. ，向零截断后得到 -2 。

# 提示：
# -231 <= dividend, divisor <= 231 - 1
# divisor != 0


class Solution:
    MIN = -(2**31)
    MAX = 2**31 - 1

    def div(self, a, b):
        """除数不能为0 且 a，b不能是整数最小值"""
        if a == 0:
            return 0

        x = a if a > 0 else -a
        y = b if b > 0 else -b
        res = 0
        i = 30
        while i >= 0:
            if (x >> i) >= y:  # 除法转化为减法
                res |= 1 << i
                x -= (y << i) & 0xFFFFFFFF
            i -= 1
        return -res if (a < 0) ^ (b < 0) else res

    def divide(self, dividend: int, divisor: int) -> int:

        if divisor == 0:
            raise ZeroDivisionError("can't division by zero !")

        a, b = dividend, divisor

        if a == self.MIN and b == self.MIN:
            # a和b都是整数最小
            return 1

        if a != self.MIN and b != self.MIN:
            # a和b都不是整数最小，那么正常去除
            return self.div(a, b)

        if b == self.MIN:
            # a不是整数最小，b是整数最小
            return 0

        if b == -1:
            # a是整数最小，b是-1，返回整数最大，因为题目里明确这么说了
            return self.MAX

        # a是整数最小，b不是整数最小，b也不是-1
        a += b if b > 0 else -b
        ans = self.div(a, b)
        offset = -1 if b > 0 else 1
        return ans + offset


if __name__ == "__main__":
    s = Solution()

    dividend = 10
    divisor = 3
    print(s.divide(dividend, divisor))

    dividend = 7
    divisor = -3
    print(s.divide(dividend, divisor))

    dividend = -2147483648
    divisor = 1
    print(s.divide(dividend, divisor))
