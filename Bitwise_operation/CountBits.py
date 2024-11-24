# 给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。

# 示例 1：
# 输入：n = 2
# 输出：[0,1,1]
# 解释：
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 示例 2：
# 输入：n = 5
# 输出：[0,1,1,2,1,2]
# 解释：
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101


def countBits(n: int) -> list[int]:
    """动态规划"""
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        # i&(i-1) 去掉 i 的最低位 1
        bits[i] = bits[i & (i - 1)] + 1
    return bits


def countBits_v2(n: int) -> list[int]:
    """利用奇偶性来解决"""
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        # bits[i] = bits[i >> 1] + (i & 1)
        if i & 1:  # i是奇数
            bits[i] = bits[i - 1] + 1
        else:
            bits[i] = bits[i >> 1]
    return bits


if __name__ == "__main__":
    n = 7
    print(countBits(n))
    print(countBits_v2(n))
