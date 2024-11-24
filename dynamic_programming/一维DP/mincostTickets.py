# 983. 最低票价 - M
# 在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。
# 在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365 的整数。
# 火车票有 三种不同的销售方式 ：
# 一张 为期一天 的通行证售价为 costs[0] 美元；
# 一张 为期七天 的通行证售价为 costs[1] 美元；
# 一张 为期三十天 的通行证售价为 costs[2] 美元。
# 通行证允许数天无限制的旅行。
# 例如，如果我们在第 2 天获得一张 为期 7 天 的通行证，那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。
# 返回 你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费 。

# 示例 1：
# 输入：days = [1,4,6,7,8,20], costs = [2,7,15]
# 输出：11
# 解释：
# 例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
# 在第 1 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 1 天生效。
# 在第 3 天，你花了 costs[1] = $7 买了一张为期 7 天的通行证，它将在第 3, 4, ..., 9 天生效。
# 在第 20 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 20 天生效。
# 你总共花了 $11，并完成了你计划的每一天旅行。
# 示例 2：
# 输入：days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# 输出：17
# 解释：
# 例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
# 在第 1 天，你花了 costs[2] = $15 买了一张为期 30 天的通行证，它将在第 1, 2, ..., 30 天生效。
# 在第 31 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 31 天生效。
# 你总共花了 $17，并完成了你计划的每一天旅行。

# 提示：
# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days 按顺序严格递增
# costs.length == 3
# 1 <= costs[i] <= 1000


from functools import cache


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """假设第 100 天是旅行的最后一天，分类讨论：

        在第 100 天购买为期 1 天的通行证，接下来需要解决的问题为：1 到 99 天的最小花费。
        在第 94 天购买为期 7 天的通行证，接下来需要解决的问题为：1 到 93 天的最小花费。
        在第 71 天购买为期 30 天的通行证，接下来需要解决的问题为：1 到 70 天的最小花费。
        这些问题都是和原问题相似的、规模更小的子问题，可以用递归解决。"""
        last_day = days[-1]
        days = set(days)

        # 记忆化搜索
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int) -> int:
            if i <= 0:
                return 0
            if i not in days:
                return dfs(i - 1)
            return min(
                dfs(i - 1) + costs[0], dfs(i - 7) + costs[1], dfs(i - 30) + costs[2]
            )

        return dfs(last_day)

    def mincostTickets2(self, days: list[int], costs: list[int]) -> int:
        """1:1 翻译成递推"""
        last_day = days[-1]
        days = set(days)
        f = [0] * (last_day + 1)
        for i in range(1, last_day + 1):
            if i not in days:
                f[i] = f[i - 1]
            else:
                f[i] = min(
                    f[i - 1] + costs[0],
                    f[max(i - 7, 0)] + costs[1],
                    f[max(i - 30, 0)] + costs[2],
                )
        return f[-1]

    def mincostTickets3(self, days: list[int], costs: list[int]) -> int:
        """三指针优化"""
        f = [0] * (len(days) + 1)
        j = k = 0
        for i, d in enumerate(days):
            while days[j] <= d - 7:
                j += 1
            while days[k] <= d - 30:
                k += 1
            f[i + 1] = min(f[i] + costs[0], f[j] + costs[1], f[k] + costs[2])
        return f[-1]
