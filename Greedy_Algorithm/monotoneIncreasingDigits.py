# 当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。
# 给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。

# 示例 1:
# 输入: n = 10
# 输出: 9
# 示例 2:
# 输入: n = 1234
# 输出: 1234
# 示例 3:
# 输入: n = 332
# 输出: 299


def monotoneIncreasingDigits(n: int) -> int:
    if n < 10:
        return max(n-1,0)
    digits = list(str(n))
    flag = len(digits)
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] < digits[i - 1]:
            digits[i - 1] = str(int(digits[i - 1]) - 1)
            flag = i
    
    if int(digits[flag - 1]) == 0:
            digits[flag - 1] = ''

    if flag == 0:   # 所有数字都是单调递增的
        return int("".join(digits))
    else:           # 部分数字不是单调递增的，第一个数字减一，后面的数字都设为9
        for i in range(flag, len(digits)):
            digits[i] = "9"
        return int("".join(digits))


if __name__ == "__main__":
    n = 0
    print(monotoneIncreasingDigits(n))
    
    n = 10
    print(monotoneIncreasingDigits(n))

    n = 1234
    print(monotoneIncreasingDigits(n))

    n = 332
    print(monotoneIncreasingDigits(n))
