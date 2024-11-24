# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用 一次 。
# 集不能包含重复的组合。 

# 示例 1:
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 示例 2:
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]


class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        self.ans = []
        # selected = set()
        self.backtrack2(sorted(candidates), target, [], 0)
        return self.ans
    
    # def backtrack(self,candidates, target, res, index, selected):
    #     if index == len(candidates):
    #         return
    #     if target == 0:
    #         self.ans.append(tuple(sorted(res, reverse=False)))
    #         return

    #     self.backtrack(candidates, target, res, index + 1, selected)        # 不选candidates[index]
    #     num = candidates[index]
    #     if num <= target and index not in selected:
    #         res.append(num)
    #         selected.add(index)
    #         self.backtrack(candidates, target - num, res, index, selected)
    #         res.pop()
    #         selected.remove(index)
            
    def backtrack2(self, candidates, target, res, index):
        if target == 0:
            self.ans.append(res[:])       # 必须答案是res的副本，要不然回溯的时候res会发生变化
            return

        for i in range(index, len(candidates)):
            num = candidates[i]
            if num > target:
                break
            if i > index and candidates[i-1] == num:
                continue
            res.append(num)
            self.backtrack2(candidates, target - num, res, i + 1)       # 注意是i+1，不是index+1
            res.pop()
    
    
    def combinationSum2_v2(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break

                if index > begin and candidates[index - 1] == candidates[index]:
                    continue

                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res



if __name__ == "__main__":
    s = Solution()
    candidates = [2, 2, 3, 4, 5, 7]
    target = 7
    print(s.combinationSum2(candidates, target))
    print(s.combinationSum2_v2(candidates,target))
    print()
    

    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(s.combinationSum2(candidates, target))
    print(s.combinationSum2_v2(candidates,target))
    print()
    
    
    candidates = [2,5,2,1,2]
    target = 5
    print(s.combinationSum2(candidates, target))
    print(s.combinationSum2_v2(candidates,target))
    print()
    
    
    