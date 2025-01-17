#
# * 224. 基本计算器
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
# 示例 1：
# 输入：s = "1 + 1"
# 输出：2
# 示例 2：
# 输入：s = " 2-1 + 2 "
# 输出：3
# 示例 3：
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23

# 提示：
# 1 <= s.length <= 3 * 105
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式
# '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
# '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
# 输入中不存在两个连续的操作符
# 每个数字和运行的计算将适合于一个有符号的 32位 整数


class Solution(object):
    def calculate(self, s):
        res, num, sign = 0, 0, 1  # 初始化当前结果、当前处理的数字和当前符号
        stack = []  # 用于存储每个括号前的计算结果和符号

        for c in s:
            if c.isdigit():
                # 处理多位数的情况
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                # 遇到符号，更新当前结果，并重置num以用于下一个数字的计算
                # 使用之前的符号计算之前的数字
                res += sign * num
                num = 0  # 重置num
                # 设置新的符号
                sign = 1 if c == "+" else -1
            elif c == "(":
                # 遇到左括号时，将当前的计算结果和符号入栈
                # 然后重置res和sign以计算括号内的表达式
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                # 遇到右括号时，计算括号内的表达式的结果
                # 并将其与栈顶的符号和之前的结果相加
                res += sign * num
                num = 0
                # 用括号前的符号乘以括号内的结果
                res *= stack.pop()
                # 然后加上括号前的结果
                res += stack.pop()
        # 对表达式最后的数字进行计算
        res += sign * num
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "(1+(4+5+2)-3)+(6+8)"
    print(sol.calculate(s))
