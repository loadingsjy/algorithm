# * 求最大公约数
# 1) 欧几里得算法的过程 : 辗转相除法
# 2) 正确性的证明过程见代码注释部分，我润色的证明过程非常好懂，不过直接记忆过程即可
# 3) 求gcd(a,b)，其中a>b，时间复杂度为O((log a)的3次方)，时间复杂度证明略，这个复杂度足够好了
# 4) 简单转化就可以求最小公倍数
# 5) 更高效求最大公约数的Stein算法、由最大公约数扩展出的“裴蜀定理”，比赛同学有兴趣可以继续研究
# 6) 不比赛的同学，哪怕你的目标是最顶级的公司应聘、还是考研，掌握这个只有一行的函数已经足够！

# * 同余原理
# 1) 介绍背景
# 2) 加法、乘法每一步计算完后直接取模，减法则为(a-b+m)%m
# 3) 要确保过程中不溢出，所以往往乘法运算的用long类型做中间变量
# 4) 除法的同余需要求逆元，会在【必备】课程里讲述，较难的题目才会涉及


# a 与 b 的最大公约数 等于 b 与 a%b 的最大公约数
def gcd(a, b):
    """求a与b的最大公约数，时间复杂度O((loga)^3)"""

    # 证明辗转相除法就是证明如下关系：
    # gcd(a, b) = gcd(b, a % b)
    # 假设a % b = r，即需要证明的关系为：gcd(a, b) = gcd(b, r)
    # 证明过程：
    # 因为a % b = r，所以如下两个等式必然成立
    # 1) a = b * q + r，q为0、1、2、3....中的一个整数
    # 2) r = a − b * q，q为0、1、2、3....中的一个整数
    # 假设u是a和b的公因子，则有: a = s * u, b = t * u
    # 把a和b带入2)得到，r = s * u - t * u * q = (s - t * q) * u
    # 这说明 : u如果是a和b的公因子，那么u也是r的因子
    # 假设v是b和r的公因子，则有: b = x * v, r = y * v
    # 把b和r带入1)得到，a = x * v * q + y * v = (x * q + y) * v
    # 这说明 : v如果是b和r的公因子，那么v也是a的公因子
    # 综上，a和b的每一个公因子 也是 b和r的一个公因子，反之亦然
    # 所以，a和b的全体公因子集合 = b和r的全体公因子集合
    # 即gcd(a, b) = gcd(b, r)
    # 证明结束
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    """求a与b的最小公倍数"""
    return a / gcd(a, b) * b
