# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

# 示例 1：
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# 示例 2：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res, path = [], []
        selected = [False] * n

        def dfs(i):
            if i == n:
                res.append(path[:])
                return
            for k, num in enumerate(nums):
                if selected[k] or (k > 0 and nums[k] == nums[k - 1] and not selected[k - 1]):
                    '''
                    这句话可以翻译为 遇到相同的节点 要填后面的节点就一定先填过前面的节点 什么意思？ 
                    假设三个1 分别为 1a 1b 1c 要想填1b 就一定之前填过1a 要想填过1c 就一定填过1b 那么三个1都被填充的顺序就一定为1a 1b 1c
                    同理可以把 !vis[i - 1]换成vis[i-1] 也能通过 此时意思就是要想填i 就必须没填过i-1 顺序就是1c 1b 1a
                    此外!vis[i - 1]会比vis[i-1] 快很多： 大家可以画个树状图，
                    原因在于!vis[i - 1] 在遇到相同节点时，会一次性取出，而vis[i-1] 则是试错了前面所有的才找到对的
                    '''
                    continue
                path.append(num)
                selected[k] = True
                dfs(i + 1)
                path.pop()
                selected[k] = False
        dfs(0)
        return res


    def permuteUnique_ii(self, nums: list[int]) -> list[list[int]]:
        """全排列 II"""
        res = []

        def backtrack(state: list[int], choices: list[int], selected: list[bool], res: list[list[int]]):
            """回溯算法：全排列 II"""
            # 当状态长度等于元素数量时，记录解
            if len(state) == len(choices):
                res.append(list(state))
                return
            # 遍历所有选择
            duplicated = set[int]()
            for i, choice in enumerate(choices):
                # 剪枝：不允许重复选择元素 且 不允许重复选择相等元素
                if not selected[i] and choice not in duplicated:
                    # 尝试：做出选择，更新状态
                    duplicated.add(choice)  # 记录选择过的元素值
                    selected[i] = True
                    state.append(choice)
                    # 进行下一轮选择
                    backtrack(state, choices, selected, res)
                    # 回退：撤销选择，恢复到之前的状态
                    selected[i] = False
                    state.pop()

        backtrack(state=[], choices=nums, selected=[False] * len(nums), res=res)
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2]
    print(s.permuteUnique(nums))
    print(s.permuteUnique_ii(nums))
