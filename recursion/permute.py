# 全排列
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 示例 2：
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
# 示例 3：
# 输入：nums = [1]
# 输出：[[1]]

# 提示：
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# nums 中的所有整数 互不相同


class Solution:
    def permute1(self, nums: list[int]) -> list[list[int]]:
        ans = []
        n = len(nums)

        def dfs(i):
            if i == n:
                return ans.append(nums[:])
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        dfs(0)
        return ans

    def permute2(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res, path = [], []

        def dfs(i):
            if i == n:
                res.append(path[:])
                return
            for j in range(0, n):
                if nums[j] not in path:
                    path.append(nums[j])
                    dfs(i + 1)
                    path.pop()

        dfs(0)
        return res

    def permute3(self, nums: list[int]) -> list[list[int]]:
        """最优写法"""
        n = len(nums)
        res, path = [], []
        selected = [False] * n

        def dfs(i):
            if i == n:
                res.append(path[:])
                return
            for k, num in enumerate(nums):
                if not selected[k]:
                    selected[k] = True
                    path.append(num)
                    dfs(i + 1)
                    path.pop()
                    selected[k] = False

        dfs(0)
        return res

    def permute4(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        path = [0] * n

        # 代表目前在选第几个数了，s表示目前可选的集合
        def dfs(i, s):
            if i == n:
                ans.append(path[:])
                return
            for x in s:
                path[i] = x
                dfs(i + 1, s - {x})

        dfs(0, set(nums))
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    print(s.permute1(nums))
    print(s.permute2(nums))
    print(s.permute3(nums))
