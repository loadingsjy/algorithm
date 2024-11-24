# 给定一个字符串，如果该字符串符合人们日常书写的一个整数格式，返回int类型的这个数；如果不符合或者越界返回-1或者报错。

# 1)除了数字之外只允许有'-'
# 2)如果有'-',一定是开头，且后序必须有数字只出现一次，且后面数字不是0
# 3)如果开头为0，后序必无字符
import sys


def isVaild(s: str):
    if not s:
        return False
    if s[0] != "-" and (s[0] < "0" or s[0] > "9"):
        return False

    if s[0] == "-" and (len(s) == 1 or s[1] == "0"):
        return False

    if s[0] == "0" and len(s) > 1:
        return False

    for i in range(1, len(s)):
        if s[i] < "0" or s[i] > "9":
            return False

    return True


def convertToInt(s: str):
    s = list(s)
    if not isVaild(s):
        raise ValueError("can not convert to int")
    neg = True if s[0] == "-" else False
    # MAX_INT = sys.maxsize
    MIN_INT = -sys.maxsize - 1
    minq = MIN_INT // 10
    minr = MIN_INT % 10
    print(minq, minr)
    res = 0
    cur = 0
    for i in range(1 if neg else 0, len(s)):
        cur = ord("0") - ord(s[i])
        # 中途转化的时候溢出
        if (res < minq) or (res == minq and cur < minr):
            raise ValueError("out of range")
        res = res * 10 + cur
    if not neg and res == MIN_INT:
        raise ValueError("out of range")
    return res if neg else -res


if __name__ == "__main__":

    print("sys.maxsize: ", sys.maxsize)
    print("sys.minsize: ", -sys.maxsize - 1)
    
    print(isVaild('0123'))
    print(isVaild('-123'))
    print(isVaild('123a'))
    print(isVaild('0'))
    print(isVaild('-0'))
    print(isVaild('00'))
    
    print(convertToInt("123"))
    print(convertToInt("9223372036854775807"))
    
    print(r'a\b\c')
