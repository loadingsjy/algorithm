# 七个不同的符号代表罗马数字，其值如下：

# 符号 值
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000
# 罗马数字是通过添加从最高到最低的小数位值的转换而形成的。将小数位值转换为罗马数字有以下规则：

# 如果该值不是以 4 或 9 开头，请选择可以从输入中减去的最大值的符号，将该符号附加到结果，减去其值，然后将其余部分转换为罗马数字。
# 如果该值以 4 或 9 开头，使用 减法形式，表示从以下符号中减去一个符号，例如 4 是 5 (V) 减 1 (I): IV ，9 是 10 (X) 减 1 (I)：IX。仅使用以下减法形式：4 (IV)，9 (IX)，40 (XL)，90 (XC)，400 (CD) 和 900 (CM)。
# 只有 10 的次方（I, X, C, M）最多可以连续附加 3 次以代表 10 的倍数。你不能多次附加 5 (V)，50 (L) 或 500 (D)。如果需要将符号附加4次，请使用 减法形式。
# 给定一个整数，将其转换为罗马数字。

# 示例 1：
# 输入：num = 3749
# 输出： "MMMDCCXLIX"
# 解释：
# 3000 = MMM 由于 1000 (M) + 1000 (M) + 1000 (M)
#  700 = DCC 由于 500 (D) + 100 (C) + 100 (C)
#   40 = XL 由于 50 (L) 减 10 (X)
#    9 = IX 由于 10 (X) 减 1 (I)
# 注意：49 不是 50 (L) 减 1 (I) 因为转换是基于小数位
# 示例 2：
# 输入：num = 58
# 输出："LVIII"
# 解释：
# 50 = L
#  8 = VIII
# 示例 3：
# 输入：num = 1994
# 输出："MCMXCIV"
# 解释：
# 1000 = M
#  900 = CM
#   90 = XC
#    4 = IV


class Solution:
    def intToRoman(self, num: int) -> str:
        MAPPING = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        ans = ""
        l = len(str(num))
        for i, n in enumerate(str(num)):
            # 当前是什么位（个位：1，十位：10，百位：10，千位：1000）
            wei = 10 ** (l - i - 1)
            n = int(n)
            if n == 4 or n == 9:
                ans += MAPPING[wei] + (MAPPING[(n + 1) * wei])
            elif n <= 3:
                ans += MAPPING[wei] * n
            else:
                ans += MAPPING[5 * wei] + MAPPING[wei] * (n - 5)
        return ans

    def intToRoman2(self, num: int) -> str:
        """建立一个数值-符号对的列表 valueSymbols，按数值从大到小排列(包括400,900,40,90,4,9)。
        遍历 valueSymbols 中的每个数值-符号对，若当前数值 value 不超过 num，则从 num 中不断减去 value，
        直至 num 小于 value，然后遍历下一个数值-符号对。若遍历中 num 为 0 则跳出循环。"""

        VALUE_SYMBOLS = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        roman = list()
        for value, symbol in VALUE_SYMBOLS:
            while num >= value:
                num -= value
                roman.append(symbol)
            if num == 0:
                break
        return "".join(roman)

    def intToRoman3(self, num: int) -> str:
        """硬编码数字"""
        THOUSANDS = ["", "M", "MM", "MMM"]
        HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (
            THOUSANDS[num // 1000]
            + HUNDREDS[num % 1000 // 100]
            + TENS[num % 100 // 10]
            + ONES[num % 10]
        )


if __name__ == "__main__":
    s = Solution()
    num = 3749
    print(s.intToRoman(num))
    print(s.intToRoman2(num))
    print(s.intToRoman3(num))

    print()
    num = 58
    print(s.intToRoman(num))
    print(s.intToRoman2(num))
    print(s.intToRoman3(num))
    print()

    num = 1994
    print(s.intToRoman(num))
    print(s.intToRoman2(num))
    print(s.intToRoman3(num))
