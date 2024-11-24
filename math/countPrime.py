import timeit
# 统计1~n之间质数的个数


# def isPrime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     for i in range(2, i**(0.5)+1):
#         if n % i == 0:
#             return False
#     return True


# 埃筛法 时间复杂度：O(n * log(logn) )
# 每个数划掉他的所有倍数
def eratosthenes(n):
    is_prime = [True] * n  # True代表质数，False代表合数，isprime[i] = True代表i是质数
    primes = []
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n, i):  # i的倍数后面无需计算，肯定是合数
                is_prime[j] = False
    return primes

# 欧拉筛（线性筛） 时间复杂度: O(n)
# 每个合数只被划掉一次
# 对于每个数x， 划掉x乘上 <=lpf[x] 的合数，lpf[x]值得时x的最小质因子
def Euler_Sieve(n):
    is_prime = [True] * n  # True代表质数，False代表合数，isprime[i] = True代表i是质数
    primes = []
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if p * i >= n:
                break
            is_prime[i * p] = False
            if i % p == 0:
                break
    return primes


if __name__ == "__main__":
    # print(eratosthenes(100))
    # print(len(eratosthenes(1000)))

    # print(Euler_Sieve(100))
    # print(len(Euler_Sieve(1000)))
    
    count = 100
    execution_time1 = timeit.timeit(
        "eratosthenes(1000000)", globals=globals(), number=count
    )
    print(f"执行{count}次的时间: {execution_time1}秒")
    execution_time1 = timeit.timeit(
        "Euler_Sieve(1000000)", globals=globals(), number=count
    )
    print(f"执行{count}次的时间: {execution_time1}秒")
