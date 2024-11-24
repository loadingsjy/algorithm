#
# * 90. 子集 II - M
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的 子集（幂集）。
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

# 示例 1：
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]

# 提示：
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
import copy


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """左神写法"""
        nums.sort()
        ans = []
        n = len(nums)
        path = [""] * n

        def dfs(i: int, size) -> None:
            """i: 当前正在处理nums[i]（选或不选），size: 当前选好的数字的数量"""
            if i == n:
                ans.append(path[:size])
                return

            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            # 当前选择的数字要0个
            dfs(j, size)
            while i < j:
                path[size] = nums[i]
                size += 1
                # 每次多选一个相同的数
                dfs(j, size)
                i += 1

        dfs(0, 0)
        return ans

    def subsetsWithDup2(self, nums: list[int]) -> list[list[int]]:
        """代码随想录写法：使用used数组"""
        result = []
        path = []
        nums.sort()
        used = [False] * len(nums)

        def backtrack(nums, startIdx):
            result.append(path[:])
            for i in range(startIdx, len(nums)):
                if i > startIdx and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtrack(nums, i + 1)
                path.pop()
                used[i] = 0

        backtrack(nums, 0)
        return result

    def subsetsWithDup3(self, nums: list[int]) -> list[list[int]]:
        """代码随想录写法：不使用used数组"""
        res = []
        path = []
        nums.sort()  # 去重需要先对数组进行排序

        def backtracking(nums, startIndex):
            # 终止条件
            res.append(path[:])
            # if startIndex == len(nums):   # 这行可以不写，因为startIndex == len(nums)后不会进入下面的循环
            #     return

            # for循环
            for i in range(startIndex, len(nums)):
                # 树层去重
                if i > startIndex and nums[i] == nums[i - 1]:  # 去重
                    continue
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()

        backtracking(nums, 0)
        return res

    def subsetsWithDup4(self, nums):
        """负雪明烛写法"""
        res, path = [], []
        nums.sort()
        n = len(nums)

        def dfs(index):
            """每个 path 是否满足题目的条件： 任何一个 path 都是子集，都满足条件，都要放到 res 中"""
            res.append(copy.deepcopy(path))
            for i in range(index, n):
                if i > index and nums[i] == nums[i - 1]:  # 剪枝
                    continue
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res

    def subsetsWithDup5(self, nums: list[int]) -> list[list[int]]:
        """用set去重，速度比剪枝方法慢"""
        nums.sort()
        s = set()

        def dfs(path, idx):
            if idx == len(nums):
                s.add(tuple(path))
                return
            dfs(path + [nums[idx]], idx + 1)
            dfs(path, idx + 1)

        dfs([], 0)
        return list(s)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 2]
    print(s.subsetsWithDup(nums))
    print(s.subsetsWithDup2(nums))
    print(s.subsetsWithDup3(nums))
    print(s.subsetsWithDup4(nums))
    print(s.subsetsWithDup5(nums))
