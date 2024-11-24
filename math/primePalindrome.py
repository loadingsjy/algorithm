# 回文质数:
# 给你一个整数 n ，返回大于或等于 n 的最小 回文质数。
# 一个整数如果恰好有两个除数：1 和它本身，那么它是 质数 。注意，1 不是质数。

# 例如，2、3、5、7、11 和 13 都是质数。
# 一个整数如果从左向右读和从右向左读是相同的，那么它是 回文数 。
# 例如，101 和 12321 都是回文数。
# 测试用例保证答案总是存在，并且在 [2, 2 * 108] 范围内。

# 示例 1：
# 输入：n = 6
# 输出：7
# 示例 2：
# 输入：n = 8
# 输出：11
# 示例 3：
# 输入：n = 13
# 输出：101

# 提示：
# 1 <= n <= 10^8


class Solution:
    def __init__(self):
        # self.primes = self.eratosthenes(10**7+1)
        pass

    def isPalindrome(self, n):
        temp = n
        reverse_n = 0
        while temp:
            reverse_n = 10 * reverse_n + temp % 10
            temp //= 10
        return reverse_n == n

    def primePalindrome(self, n: int) -> int:
        """方法超时"""
        primes = self.eratosthenes(n * 1000)
        primes_and_Palindromes = list(filter(self.isPalindrome, primes))
        index = self.binary_frist_right_larger(primes_and_Palindromes, n)
        if index == -1:
            return -1
        return primes_and_Palindromes[index]

    def eratosthenes(self, n):
        """埃筛法找到比n小的所有质数"""
        primes = []
        isprime = [
            True
        ] * n  # True代表质数，False代表合数，isprime[i] = True代表i是质数
        # count = 0
        for i in range(2, n):
            if isprime[i]:
                # count += 1
                primes.append(i)
                for j in range(i * i, n, i):  # i的倍数后面无需计算，肯定是合数
                    isprime[j] = False
        # print(len(primes))
        return primes

    def binary_frist_right_larger(self, arr, num):
        """二分查找第一个比x大(或者等于)的数的下标"""
        low = 0
        high = len(arr) - 1

        if arr[high] <= num:
            return -1

        while low < high:
            mid = (low + high) // 2
            if arr[mid] <= num:
                low = mid + 1
            else:
                high = mid - 1

        if low > 0 and arr[low - 1] == num:
            return low - 1
        else:
            return low

    def primePalindrome2(self, N):
        """遍历法：
        对于每个回文根，找对应的两个回文串（一个奇数长度，一个偶数长度）。对于 k 长度的回文根，会产生长度为 2∗k−1 和 2∗k−1 的回文串。
        当检查回文串的时候，需要先检查小的 2k−1 长度的，这里直接把数字变成字符串来检查是否对称。
        """

        def is_prime(n):
            return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))

        for length in range(1, 6):
            # Check for odd-length palindromes
            for root in range(10 ** (length - 1), 10**length):
                s = str(root)
                x = int(s + s[-2::-1])  # eg. s = '123' to x = int('12321')
                if x >= N and is_prime(x):
                    # return x
                    # If we didn't check for even-length palindromes:
                    # 知识点： “偶数长度的回文数”中只有11是素数，其他的都可以被11整除。
                    return min(x, 11) if N <= 11 else x

            # Check for even-length palindromes
            # for root in range(10**(length - 1), 10**length):
            #     s = str(root)
            #     x = int(s + s[-1::-1]) #eg. s = '123' to x = int('123321')
            #     if x >= N and is_prime(x):
            #         return x

    def primePalindrome3(self, N):
        """数学法: 遍历所有数字，检查是不是回文串。如果是，检查是不是素数，如果当前数字长度为 8，可以跳过检查，因为不存在8长度的素数。"""

        def is_prime(n):
            return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x //= 10
            return ans

        while True:
            if N == reverse(N) and is_prime(N):
                return N
            N += 1
            if 10**7 < N < 10**8:
                N = 10**8


if __name__ == "__main__":
    s = Solution()
    # print(s.isPalindrome(2))
    # print(s.isPalindrome(12321))
    # print(s.isPalindrome(1231))
    # print(s.primePalindrome(13))

    print(s.primePalindrome2(13))
    print(s.primePalindrome3(13))
