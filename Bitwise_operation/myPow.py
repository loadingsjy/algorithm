# 50. Pow(x, n)

# 实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。

# 示例 1：
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
# 示例 2：
# 输入：x = 2.10000, n = 3
# 输出：9.26100
# 示例 3：
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25

# 提示：
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# n 是一个整数
# 要么 x 不为零，要么 n > 0 。
# -10^4 <= x^n <= 10^4


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:  # x^n = (1/x) ^ n
            n = -n
            x = 1 / x
        ans = 1
        while n > 0:  # 从低到高枚举 n 的每个比特位
            if n & 1:  # 这个比特位是 1
                ans *= x  # 把 x 乘到 ans 中
            n >>= 1  # x 自身平方
            x *= x  # 继续枚举下一个比特位
        return ans

    def myPow2(self, x: float, n: int) -> float:
        """递归实现"""

        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


if __name__ == "__main__":
    sol = Solution()
    x = 2
    n = 10
    print(sol.myPow(x, n))
    print(sol.myPow2(x, n))
