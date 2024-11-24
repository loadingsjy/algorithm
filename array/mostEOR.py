#
# * 给定一个数组，问最多有多少个不重叠的非空区间，使得每个区间内数字的异或和(xor)都等于0


def MostEOR(arr):
    xor = 0
    n = len(arr)
    dp = [0] * n

    last_xor_index = dict()
    last_xor_index[0] = (
        -1
    )  # key:从0位置出发某个前缀异或和, value:这个前缀异或和最晚出现的位置（index)

    for i in range(n):
        xor ^= arr[i]
        if xor in last_xor_index:
            pre = last_xor_index[xor]
            if pre == -1:
                dp[i] = 1
            else:
                dp[i] = dp[pre] + 1

        if i > 0:
            dp[i] = max(dp[i - 1], dp[i])

        last_xor_index[xor] = i

    return dp[-1]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 0, 5, 0, 1, 1]

    print(MostEOR(arr))

    arr = [1, 2, 3, 0, 4]
    print(MostEOR(arr))
