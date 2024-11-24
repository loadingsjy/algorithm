# 给定一个候选人编号的集合 cand 和一个目标数 target ，找出 cand 中所有可以使数字和为 target 的组合。
# * cand 中的每个数字在每个组合中只能使用 一次 。
# 注意：解集不能包含重复的组合。

# 示例 1:
# 输入: cand = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 示例 2:
# 输入: cand = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]


class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum2(self, cand: list[int], target: int) -> list[list[int]]:
        self.ans = []
        # selected = set()
        self.backtrack(sorted(cand), target, [], 0)
        return self.ans

    def backtrack(self, cand, target, res, index):
        if target == 0:
            # 必须答案是res的副本，要不然回溯的时候res会发生变化
            self.ans.append(res[:])
            return

        for i in range(index, len(cand)):
            num = cand[i]
            if num > target:
                break
            if i > index and cand[i - 1] == num:
                continue
            res.append(num)
            # 注意是i+1，不是index+1
            self.backtrack(cand, target - num, res, i + 1)
            res.pop()
