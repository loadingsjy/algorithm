#
# * 726. 原子的数量 - H
# 给你一个字符串化学式 formula ，返回 每种原子的数量 。
# 原子总是以一个大写字母开始，接着跟随 0 个或任意个小写字母，表示原子的名字。
# 如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。

# 例如，"H2O" 和 "H2O2" 是可行的，但 "H1O2" 这个表达是不可行的。
# 两个化学式连在一起可以构成新的化学式。
# 例如 "H2O2He3Mg4" 也是化学式。
# 由括号括起的化学式并佐以数字（可选择性添加）也是化学式。
# 例如 "(H2O2)" 和 "(H2O2)3" 是化学式。
# 返回所有原子的数量，格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

# 示例 1：
# 输入：formula = "H2O"
# 输出："H2O"
# 解释：原子的数量是 {'H': 2, 'O': 1}。
# 示例 2：
# 输入：formula = "Mg(OH)2"
# 输出："H2MgO2"
# 解释：原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
# 示例 3：
# 输入：formula = "K4(ON(SO3)2)2"
# 输出："K4N2O14S4"
# 解释：原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。

# 提示：
# 1 <= formula.length <= 1000
# formula 由英文字母、数字、'(' 和 ')' 组成
# formula 总是有效的化学式
from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """化学式解析：
        1.从左到右遍历该化学式，并使用哈希表记录当前层遍历到的原子及其数量，因此初始时需将一个空的哈希表压入栈中。对于当前遍历的字符：
            1)如果是左括号，将一个空的哈希表压入栈中，进入下一层。
            2)如果不是括号，则读取一个原子名称，若后面还有数字，则读取一个数字，否则将该原子后面的数字视作 1。
                然后将原子及数字加入栈顶的哈希表中。
            3)如果是右括号，则说明遍历完了当前层，若括号右侧还有数字，则读取该数字 num，否则将该数字视作 1。
                然后将栈顶的哈希表弹出，将弹出的哈希表中的原子数量与 num 相乘，加到上一层的原子数量中。
        2.遍历结束后，栈顶的哈希表即为化学式中的原子及其个数。遍历哈希表，取出所有「原子-个数」对加入数组中，对数组按照原子字典序排序，然后遍历数组，按题目要求拼接成答案。
        """

        n = len(formula)

        def getAtom(idx):
            """返回原子名称，下个index"""
            atom = ""
            atom += formula[idx]
            idx += 1
            while idx < n and formula[idx].islower():
                atom += formula[idx]
                idx += 1
            return atom, idx

        def getNum(idx):
            """返回数字，下个index"""
            res = 0
            while idx < n and formula[idx].isnumeric():
                res = res * 10 + int(formula[idx])
                idx += 1
            return 1 if res == 0 else int(res), idx

        name = ""
        cnt = 0
        stack = [Counter()]
        i = 0
        while i < n:
            ch = formula[i]
            if ch == "(":
                stack.append(Counter())
                i += 1
            elif ch == ")":
                i += 1
                cnt, i = getNum(i)
                t = stack.pop()
                for key, value in t.items():
                    stack[-1][key] += cnt * value
                cnt = 0
                name = ""
            else:
                name, idx = getAtom(i)
                cnt, i = getNum(idx)
                stack[-1][name] += cnt
                cnt = 0
                name = ""

        res_count = stack[-1]
        ans = ""
        for key, value in sorted(res_count.items(), key=lambda x: x[0]):
            ans += key + (str(value) if value != 1 else "")
        return ans

    def countOfAtoms_re(self, formula: str) -> str:
        """递归"""
        n = len(formula)
        where = 0  # 当前解析到哪个index了

        def fill(ans, name, pre, cnt):
            if name or len(pre) != 0:
                cnt = 1 if cnt == 0 else cnt
                if name:
                    ans[name] += cnt
                else:
                    for key, value in pre.items():
                        ans[key] += value * cnt

        def helper(i):
            """返回从i开始解析到的结果（遇到右括号就终止）：一个Counter_Map"""
            ans = Counter()  # 总表
            name = ""  # 历史原子名字
            pre = Counter()  # 之前收集到的有序表，历史的一部分
            cnt = 0  # 历史翻几倍
            nonlocal where
            while i < n and formula[i] != ")":
                ch = formula[i]
                if ch.isupper() or ch == "(":  # 遇到大写字母或者左括号，就处理历史记录
                    fill(ans, name, pre, cnt)
                    name = ""
                    pre = Counter()
                    cnt = 0
                    if ch.isupper():
                        name += ch
                        i += 1
                    else:  # 左括号
                        pre = helper(i + 1)
                        i = where + 1
                elif ch.islower():
                    name += ch
                    i += 1
                else:
                    cnt = cnt * 10 + int(ch)
                    i += 1

            fill(ans, name, pre, cnt)  # 最后
            where = i
            return ans

        ans1 = helper(0)
        res = ""
        for key, value in sorted(ans1.items(), key=lambda x: x[0]):
            res += key + (str(value) if value != 1 else "")
        return res
