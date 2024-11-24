# 367.有效的完全平方数
# 给你一个正整数 num 。如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
# 完全平方数 是一个可以写成某个整数的平方的整数。换句话说，它可以写成某个整数和自身的乘积。
# 不能使用任何内置的库函数，如  sqrt 。


# 示例 1：
# 输入：num = 16
# 输出：true
# 解释：返回 true ，因为 4 * 4 = 16 且 4 是一个整数。
# 示例 2：
# 输入：num = 14
# 输出：false
# 解释：返回 false ，因为 3.742 * 3.742 = 14 但 3.742 不是一个整数。


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """内置函数"""
        return float.is_integer(pow(num, 0.5))

    def isPerfectSquare2(self, num: int) -> bool:
        """完全平方数的特性：每个完全平方数都可以表示为从 1 开始的连续奇数之和，时间复杂度O(sqrt(n))"""
        if num < 0:
            return False
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

    def isPerfectSquare3(self, num: int) -> bool:
        """二分查找，时间复杂度：O(logn)"""
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True
        return False

    def isPerfectSquare4(self, num: int) -> bool:
        """牛顿迭代法，时间复杂度：O(logn)"""
        x0 = num
        while True:
            x1 = (x0 + num / x0) / 2
            if x0 - x1 < 1e-6:
                break
            x0 = x1
        x0 = int(x0)
        return x0 * x0 == num


if __name__ == "__main__":
    s = Solution()
    num = 1024
    print(s.isPerfectSquare(num))
    print(s.isPerfectSquare2(num))
    print(s.isPerfectSquare3(num))
    print(s.isPerfectSquare4(num))
