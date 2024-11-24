#
# * 881. 救生艇 - M
# 给定数组 people 。people[i]表示第 i 个人的体重 ，船的数量不限，每艘船可以承载的最大重量为 limit。
# 每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
# 返回 承载所有人所需的最小船数 。

# 示例 1：
# 输入：people = [1,2], limit = 3
# 输出：1
# 解释：1 艘船载 (1, 2)
# 示例 2：
# 输入：people = [3,2,2,1], limit = 3
# 输出：3
# 解释：3 艘船分别载 (1, 2), (2) 和 (3)
# 示例 3：
# 输入：people = [3,5,3,4], limit = 5
# 输出：4
# 解释：4 艘船分别载 (3), (3), (4), (5)

# 提示：
# 1 <= people.length <= 5 * 10^4
# 1 <= people[i] <= limit <= 3 * 10^4


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        """先对所有人的体重排序，再每次贪心地的选择两个人（体重一个最大 一个最小）"""

        people.sort()
        n = len(people)
        l, r = 0, n - 1
        ans = 0
        while l < r:
            if people[l] + people[r] > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            ans += 1
        if l == r and people[l] <= limit:
            ans += 1
        return ans
