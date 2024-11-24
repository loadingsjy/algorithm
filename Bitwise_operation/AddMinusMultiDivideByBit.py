# 位运算实现加减乘除，过程中不能出现任何算术运算符

# 加法：利用每一步无进位相加的结果 + 进位的结果不停计算，直到进位消失
# 减法：利用加法，和一个数字x相反数就是(~x)+1
# 乘法：回想小学时候怎么学的乘法，除此之外没别的了
# 除法：为了防止溢出，让被除数右移，而不是除数左移。从高位尝试到低位。

import ctypes


class AddMinusMultiDivideByBit:
    def __init__(self):
        pass

    def add(self, a, b):
        """位运算实现加法 如果用户传入的a+b是溢出的，则用户活该。"""
        # TODO 正数加负数有bug，已解决（ans外面加个防溢出）
        ans = a
        while b:
            ans = a ^ b  # 无进位相加
            # 右移的过程中， python 内部为了防止溢出会自动把32位扩展为64位，所以需要与上0xFFFFFFFF还原成32位
            b = ((a & b) << 1) & 0xFFFFFFFF  # 每个位置的进位信息
            a = ans
        return self.int_overflow(ans)  # ans会溢出

        # 2^32
        # MASK = 0x100000000
        # 整型最大值
        # MAX_INT = 0x7FFFFFFF
        # MIN_INT = MAX_INT + 1
        # while b != 0:
        #     计算进位
        #     carry = (a & b) << 1
        #     取余范围限制在 [0, 2^32-1] 范围内
        #     a = (a ^ b) % MASK
        #     b = carry % MASK
        # return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

    def negative(self, a):
        """取相反数"""
        return self.add(~a, 1)

    def sign(self, a):
        """获取符号位，0表示正数，1表示负数"""
        return (a >> 31) & 1

    def minus(self, a, b):
        return self.add(a, self.negative(b))

    def multi(self, a, b):
        """位运算实现乘法运算，如果用户传入的a*b是溢出的，则用户活该。"""
        result = 0
        while b != 0:
            if b & 1:  # b的最低位为1，则需要加上a
                result = self.add(result, a)
            a = a << 1
            b = (b >> 1) & 0xFFFFFFFF
        return result

    def divide(self, a, b):
        """除数不能为0 且 a，b不能是整数最小值"""
        if b == 0:
            raise ZeroDivisionError("division by zero")
        if a == 0:
            return 0

        x = a if a > 0 else self.negative(a)
        y = b if b > 0 else self.negative(b)
        res = 0
        i = 30
        while i >= 0:
            if (x >> i) >= y:
                res |= 1 << i
                x = self.minus(x, (y << i) & 0xFFFFFFFF)
            i = self.minus(i, 1)
        return self.negative(res) if (a < 0) ^ (b < 0) else res

    def is2power(self, a):
        """判断是否为2的幂"""
        # return (a & (a - 1)) == 0
        return a > 0 and a == a & -a

    def is3power(self, a):
        """判断是否为3的幂，1162261467=3^19 为无符号整数最大的3的幂"""
        return a > 0 and 1162261467 % a == 0

    def is4power(self, a):
        """判断是否为4的幂"""
        return (a & (a - 1)) == 0 and (a & 0x55555555) != 0

    def swap(self, a, b):
        """交换两个数"""
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b

    def most_right_one(self, a):
        """获取最右边的1的位置"""
        # return a & (~a + 1)
        return a & -a

    def near2power(self, n):
        """返回大于等于n的2的某次幂(最接近的)"""
        if n <= 0:
            return 1
        n -= 1
        # * 把n二进制中最右侧的1的后面都刷成1
        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16
        return n + 1

    def rangeBitwiseAnd(self, left, right):
        """返回 [left,right] 区间内所有整数的 与和，时间复杂度O(K)，K = (right二进制1的个数)"""
        while left < right:
            # 每次循环消去最右边的1，因为 left<right 会导致 这个1被与成0
            right -= right & (-right)
        return right

    def int_overflow(self, val):
        # python 内部为了防止溢出会自动把32位扩展为64位，将结果还原成没有防溢出的原来的结果
        maxint = 2147483647
        if not -maxint - 1 <= val <= maxint:
            val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
        return val

    def unsigned_right_shift(self, n, i):
        """python中 只有 有符号右移(>>)"""
        # 数字小于0，则转为32位无符号uint
        if n < 0:
            n = ctypes.c_uint32(n).value
        # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
        if i < 0:
            return -self.int_overflow(n << abs(i))
        # print(n)
        return self.int_overflow(n >> i)

    def reverseBits(self, n):
        """逆序二进制的状态
        分治思想：先相邻两个交换，再两个一组进行交换，再4个一组进行交换。。。一直进行下去
        """
        n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
        n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
        n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
        n = (n >> 16) | (n << 16)
        return n & 0xFFFFFFFF

    def reverseBits2(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = res * 2 + ((n >> i) & 1)
        return res

    def cntOnes(self, n):
        """分治思想，先求出每个位上1的个数，再合并得到两个一组1个个数，再合并得到4个一组1的个数......"""
        n = (n & 0x55555555) + (self.unsigned_right_shift(n, 1) & 0x55555555)
        n = (n & 0x33333333) + (self.unsigned_right_shift(n, 2) & 0x33333333)
        n = (n & 0x0F0F0F0F) + (self.unsigned_right_shift(n, 4) & 0x0F0F0F0F)
        n = (n & 0x00FF00FF) + (self.unsigned_right_shift(n, 8) & 0x00FF00FF)
        n = (n & 0x0000FFFF) + (self.unsigned_right_shift(n, 16) & 0x0000FFFF)
        return n & 0xFFFFFFFF

    def hammingDistance(self, x: int, y: int) -> int:
        """两个数字对应二进制位不同的位置的数目"""
        z = x ^ y
        count = 0
        while z:
            count += 1
            z &= z - 1
        return count

    def hammingDistance2(self, x: int, y: int) -> int:
        return self.cntOnes(x ^ y)


if __name__ == "__main__":
    a, b, c, d, e, h = 20, 5, -2, 4, -17, 18
    bit_calc = AddMinusMultiDivideByBit()
    print(bit_calc.sign(a))
    print(bit_calc.sign(c))
    print(bit_calc.negative(a))
    print(bit_calc.negative(c))
    print()
    print(bit_calc.add(a, b))
    print(bit_calc.add(a, c))
    print(bit_calc.add(a, e))
    print(bit_calc.minus(a, b))
    print(bit_calc.multi(a, b))
    print(bit_calc.multi(a, c))
    print(bit_calc.divide(a, b))
    print(bit_calc.divide(a, c))
    print()
    print(bit_calc.is2power(d))
    print(bit_calc.is4power(e))
    print(bit_calc.is4power(h))
    print()
    print(bit_calc.swap(a, b))
    print(bit_calc.most_right_one(h))
    print()
    print(h, "near 2 power: ", bit_calc.near2power(h))
    print("range bitwise and sum: ", bit_calc.rangeBitwiseAnd(17, 24))
    print(bin(a))
    print("reverse bits: ", bin(bit_calc.reverseBits(a)))
    print("hamming distance: ", bit_calc.hammingDistance(a, h))
    print("hamming distance: ", bit_calc.hammingDistance2(a, h))
