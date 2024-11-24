# 计算一个浮点数的立方根，不使用库函数。
# 保留一位小数。
# 数据范围：∣val∣≤20
# 输入描述：
# 待求解参数，为double类型（一个实数）
# 输出描述：
# 输出参数的立方根。保留一位小数。
# 示例:
# 输入：
# 19.9
# 输出：
# 2.7


def sqrt_3(num):
    if num == 0 or num == 1 or num == -1:
        return num

    isneg = False
    if num < 0:
        isneg = True
        num = -num

    low = 0.0
    high = num if num > 1 else 1.0

    while abs(high - low) > 1e-3:
        mid = (low + high) / 2
        if mid * mid * mid == num:
            return mid
        elif mid * mid * mid < num:
            low = mid
        else:
            high = mid
    res = round(low, ndigits=1)

    return res if not isneg else -res


if __name__ == "__main__":
    num = -19.9
    print(sqrt_3(num))

    num = 0.3
    print(sqrt_3(num))

    num = 101
    print(sqrt_3(num))
