# 假设s和m初始化，s = 'a'; m = s，再定义一下两个操作：
# 1) m = s, s = s +s
# 2) s = s + m
# 每次只能选一种操作，求最小的操作数，可以将s拼接到长度等于n


# 请保证n不是质数
# 返回所有因子的和，以及因子的个数（不包括1）
def divsSumAndCount(n):
    primeSum = 0
    count = 0
    for i in range(2, n + 1):
        while n % i == 0:
            primeSum += i
            count += 1
            n //= i

    return primeSum, count


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def minOps(n):
    if n < 2:
        return 0
    if isPrime(n):  # 要得到质数长度的s, 最少需要n-1次(2)操作
        return n - 1
    primeSumum, count = divsSumAndCount(n)
    # print(primeSumum, count)
    return primeSumum - count


if __name__ == "__main__":
    n = 7
    print(minOps(n))

    n = 12
    print(minOps(n))

    n = 15
    print(minOps(n))

    n = 20
    print(minOps(n))
