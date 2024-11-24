#
# * 772. 基本计算器 III - H
# 实现一个基本的计算器来计算简单的表达式字符串。

# 表达式字符串只包含非负整数，算符 +、-、*、/ ，左括号 ( 和右括号 ) 。整数除法需要 向下截断 。
# 你可以假定给定的表达式总是有效的。所有的中间结果的范围均满足 [-231, 231 - 1] 。
# 注意：你不能使用任何将字符串作为表达式求值的内置函数，比如 eval() 。

# 示例 1：
# 输入：s = "1+1"
# 输出：2
# 示例 2：
# 输入：s = "6-4/2"
# 输出：4
# 示例 3：
# 输入：s = "2*(5+5*2)/3+(6/2+8)"
# 输出：21

# 提示：
# 1 <= s <= 104
# s 由整数、'+'、'-'、'*'、'/'、'(' 和 ')' 组成
# s 是一个 有效的 表达式


# 作者：labuladong
# 链接：https://leetcode.cn/problems/basic-calculator/solutions/465311/chai-jie-fu-za-wen-ti-shi-xian-yi-ge-wan-zheng-j-2/


def calculate(s: str) -> int:

    def helper(s: list) -> int:
        stack = []
        sign = "+"
        num = 0

        while len(s) > 0:
            c = s.pop(0)
            if c.isdigit():
                num = 10 * num + int(c)
            # 遇到左括号开始递归计算 num
            if c == "(":
                num = helper(s)

            if (not c.isdigit() and c != " ") or len(s) == 0:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack[-1] = stack[-1] * num
                elif sign == "/":
                    # python 除法向 0 取整的写法
                    stack[-1] = int(stack[-1] / float(num))
                num = 0
                sign = c
            # 遇到右括号返回递归结果
            if c == ")":
                break

        return sum(stack)

    # 需要把字符串转成列表方便操作
    return helper(list(s))


if __name__ == "__main__":
    s = "2*(5+5*2)/3+(6/2+8)"
    print(calculate(s))

    s = "2 * (((5 + 5 * 2) + 3) + (6 / 2 + 8) * (2 + 3))"
    print(calculate(s))
