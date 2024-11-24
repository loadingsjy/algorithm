#
# 6. Z 字形变换
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
# 请你实现这个将字符串进行指定行数变换的函数：
# string convert(string s, int numRows);

# 示例 1：
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
# 示例 2：
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
# 解释：
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 示例 3：
# 输入：s = "A", numRows = 1
# 输出："A"


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """算法流程：
        1. 按顺序遍历字符串 s ：res[i] += c： 把每个字符 c 填入对应行 si；
        2. i += flag： 更新当前字符 c 对应的行索引；
        3. flag = - flag： 在达到 Z 字形转折点时，执行反向。"""
        if numRows < 2:
            return s
        n = len(s)
        res = ["" for _ in range(numRows)]
        flag = -1
        row = 0
        for c in s:
            res[row] += c
            if row == 0 or row == numRows - 1:
                flag = -flag
            row += flag
        return "".join(res)


if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    print(sol.convert(s, numRows))
