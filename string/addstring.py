# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。

# 示例 1：
# 输入：num1 = "11", num2 = "123"
# 输出："134"
# 示例 2：
# 输入：num1 = "456", num2 = "77"
# 输出："533"
# 示例 3：
# 输入：num1 = "0", num2 = "0"
# 输出："0"


def addStrings(num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        if n1 > n2:
            nums1 = num1
            nums2 = ''.join((["0"] * (n1 - n2) + list(num2)))
        elif n1 < n2:
            nums1 = ''.join((["0"] * (n2 - n1) + list(num1)))
            nums2 = num2
        else:
            nums1 = num1
            nums2 = num2

        # assert len(nums1) == len(nums2)
        i = len(nums1) - 1

        res = []
        carry = 0
        t = ord("0")
        while i >= 0:
            num = ord(nums1[i]) - t + ord(nums2[i]) - t + carry
            carry = num // 10
            res.insert(0,str(num % 10))
            i -= 1

        if carry > 0:       # 最后一位有进位
            res.insert(0,str(carry))

        return ''.join(res)


def addStrings2(num1: str, num2: str) -> str:
    res = ""
    carry = 0
    i = len(num1) - 1
    j = len(num2) - 1
    while i >= 0 or j >= 0:
        if i >= 0:
            carry += ord(num1[i]) - ord("0")
            i -= 1
        if j >= 0:
            carry += ord(num2[j]) - ord("0")
            j -= 1
        res = str(carry % 10) + res
        carry //= 10
    if carry > 0:
        res = str(carry) + res
    return res
    
    
if __name__ == '__main__':
    num1 = "11"
    num2 = "123"
    print(addStrings(num1, num2))
    print(addStrings2(num1, num2))
    print()
    
    num1 = "456"
    num2 = "68"
    print(addStrings(num1, num2))
    print(addStrings2(num1, num2))
    print()
    
    num1 = "0"
    num2 = "0"
    print(addStrings(num1, num2))
    print(addStrings2(num1, num2))
    print()
    
    num1 = "9"
    num2 = "1"
    print(addStrings(num1, num2))
    print(addStrings2(num1, num2))
    print()
    
    # num1 = "123456789"
    # num2 = "987654321"
    # print(addStrings(num1, num2))
    # print(addStrings2(num1, num2))
