#
# * 78. 子集 - M
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]

# 提示：
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(i: int) -> None:
            """输入的角度：对于输入的 nums，考虑每个 nums[i] 是选还是不选，
            由此组合出 2^n个不同的子集。dfs 中的 i 表示当前考虑到 nums[i] 选或不选。"""
            if i == n:  # 子集构造完毕
                ans.append(path.copy())  # 复制 path，也可以写 path[:]
                return

            # 不选 nums[i]
            dfs(i + 1)

            # 选 nums[i]
            path.append(nums[i])
            dfs(i + 1)
            path.pop()  # 恢复现场

        dfs(0)
        return ans

    def subsets(self, nums: list[int]) -> list[list[int]]:
        """输出的角度：枚举子集（答案）的第一个数选谁，第二个数选谁，第三个数选谁，依此类推。
        dfs 中的 i 表示现在要枚举选 nums[i] 到 nums[n−1] 中的一个数，添加到 path 末尾。
        如果选 nums[j] 添加到 path 末尾，那么下一个要添加到 path 末尾的数，就要在 nums[j+1] 到 nums[n−1] 中枚举了。
        注意：不需要在回溯中判断 i=n 的边界情况，因为此时不会进入循环，if i == n: return 这句话写不写都一样。"""
        ans = []
        path = []
        n = len(nums)

        def dfs(i: int) -> None:
            """每个 path 是否满足题目的条件： 任何一个 path 都是子集，都满足条件，都要放到 res 中"""
            ans.append(path.copy())  # 复制 path
            for j in range(i, n):  # 枚举选择的数字
                path.append(nums[j])
                dfs(j + 1)
                path.pop()  # 恢复现场

        dfs(0)
        return ans
