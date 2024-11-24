#
# * 475. 供暖器 - M
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
# 在加热器的加热半径范围内的每个房屋都可以获得供暖。
# 现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。
# 注意：所有供暖器 heaters 都遵循你的半径标准，加热的半径也一样。

# 示例 1:
# 输入: houses = [1,2,3], heaters = [2]
# 输出: 1
# 解释: 仅在位置 2 上有一个供暖器。如果我们将加热半径设为 1，那么所有房屋就都能得到供暖。
# 示例 2:
# 输入: houses = [1,2,3,4], heaters = [1,4]
# 输出: 1
# 解释: 在位置 1, 4 上有两个供暖器。我们需要将加热半径设为 1，这样所有房屋就都能得到供暖。
# 示例 3：
# 输入：houses = [1,5], heaters = [2]
# 输出：3

# 提示：
# 1 <= houses.length, heaters.length <= 3 * 104
# 1 <= houses[i], heaters[i] <= 109


class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        """遍历得到每个房间的最短供暖距离，最后取这些距离的最大值即为答案"""
        houses.sort()
        heaters.sort()
        m = len(heaters)
        ans = 0
        right = 0
        for h in houses:
            while right != m - 1 and abs(heaters[right] - h) >= abs(
                heaters[right + 1] - h
            ):
                right += 1
            ans = max(ans, abs(heaters[right] - h))
        return ans


if __name__ == "__main__":
    sol = Solution()
    houses = [1, 2, 3, 4]
    heaters = [1, 4]
    print(sol.findRadius(houses, heaters))
