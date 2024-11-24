#
# * 439. 三元表达式解析器 - M
# 给定一个表示任意嵌套三元表达式的字符串 expression ，求值并返回其结果。
# 你可以总是假设给定的表达式是有效的，并且只包含数字， '?' ，  ':' ，  'T' 和 'F' ，其中 'T' 为真， 'F' 为假。
# 表达式中的所有数字都是 一位 数(即在 [0,9] 范围内)。
# 条件表达式从右到左分组(大多数语言中都是这样)，表达式的结果总是为数字 'T' 或 'F' 。

# 示例 1：
# 输入： expression = "T?2:3"
# 输出： "2"
# 解释： 如果条件为真，结果为 2；否则，结果为 3。
# 示例 2：
# 输入： expression = "F?1:T?4:5"
# 输出： "4"
# 解释： 条件表达式自右向左结合。使用括号的话，相当于：
#  "(F ? 1 : (T ? 4 : 5))" --> "(F ? 1 : 4)" --> "4"
# or "(F ? 1 : (T ? 4 : 5))" --> "(T ? 4 : 5)" --> "4"
# 示例 3：
# 输入： expression = "T?T?F:5:3"
# 输出： "F"
# 解释： 条件表达式自右向左结合。使用括号的话，相当于：
# "(T ? (T ? F : 5) : 3)" --> "(T ? F : 3)" --> "F"
# "(T ? (T ? F : 5) : 3)" --> "(T ? F : 5)" --> "F"

# 提示:
# 5 <= expression.length <= 104
# expression 由数字, 'T', 'F', '?' 和 ':' 组成
# 保证 了表达式是一个有效的三元表达式，并且每个数字都是 一位数


class Solution:
    def parseTernary(self, expression: str) -> str:
        n = len(expression)

        stack = []
        temp = ""
        i = n - 1
        while i >= 0:
            ch = expression[i]
            if ch == ":":
                if temp:
                    stack.append(temp)
                    temp = ""
                i -= 1
            elif ch == "?":
                if temp:
                    stack.append(temp)
                choice = expression[i - 1]
                res1 = stack.pop()
                res2 = stack.pop()
                if choice == "T":
                    stack.append(res1)
                elif choice == "F":
                    stack.append(res2)
                temp = ""
                i -= 2
            else:
                temp += ch
                i -= 1

        return stack[-1]

    def parseTernary2(self, expression: str) -> str:
        # 用来标记下一个遇到的字符是条件
        is_condition = 0
        stk = []
        # 因为是从右至左结合,所以也从右至左遍历
        for i in range(len(expression) - 1, -1, -1):
            if expression[i] == ":":
                continue
            elif expression[i] == "?":  # 标记下一个遇到的字符是条件
                is_condition = 1
            else:
                if is_condition:
                    if (
                        expression[i] == "T"
                    ):  # 说明栈中的第一个元素是结果, 但要把错误结果删掉
                        res = stk[-1]
                        stk.pop()
                        stk.pop()
                        stk.append(res)
                    else:  # 说明栈中第二个元素是结果, 删掉栈顶元素即可
                        stk.pop()
                    is_condition = 0
                else:  # 当前扫描到的元素不是条件, 就是直接入栈
                    stk.append(expression[i])
        return stk[-1]

    def parseTernary3(self, expression: str) -> str:
        stack, i = [], len(expression) - 1
        while i >= 0:
            if expression[i] == "?":
                i -= 1  # expression[i] 为 "?" 时，expression[i - 1]就是条件 "T" or "F"
                cond = expression[i]  # 获取条件"T" or "F"
                t = stack.pop()  # 获取cond = "T"时的结果
                stack.pop()  # pop掉 ":"
                f = stack.pop()  # 获取cond = "F"时的结果

                if cond == "T":  # 做判断，把最终结果塞回 stack
                    stack.append(t)
                else:
                    stack.append(f)
            else:
                stack.append(expression[i])  # 不是 "?"，统统塞进 stack

            i -= 1
        return stack[-1]  # 最后只剩下最终结果在stack中

    def parseTernary4(self, expression: str) -> str:
        """递归写法"""
        if len(expression) == 1:
            return expression[0]
        pre, cur, j = 1, 0, 0
        for i in range(2, len(expression)):
            if expression[i] == "?":
                pre += 1
            elif expression[i] == ":":
                cur += 1
                if cur == pre:  # 问号和冒号数量相等时，进行递归
                    j = i
                    break
        if expression[0] == "T":
            return self.parseTernary(expression[2:j])
        else:
            return self.parseTernary(expression[j + 1 :])


if __name__ == "__main__":
    sol = Solution()
    expression = "F?1:T?4:5"
    print(sol.parseTernary(expression))
    print(sol.parseTernary2(expression))
    print(sol.parseTernary3(expression))
    print(sol.parseTernary4(expression))
