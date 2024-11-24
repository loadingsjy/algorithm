#
# * 2332. 坐上公交的最晚时间 - M

# 给你一个下标从 0 开始长度为 n 的整数数组 buses ，其中 buses[i] 表示第 i 辆公交车的出发时间。
# 同时给你一个下标从 0 开始长度为 m 的整数数组 passengers ，其中 passengers[j] 表示第 j 位乘客的到达时间。
# 所有公交车出发的时间互不相同，所有乘客到达的时间也互不相同。
# 给你一个整数 capacity ，表示每辆公交车 最多 能容纳的乘客数目。
# 每位乘客都会搭乘下一辆有座位的公交车。如果你在 y 时刻到达，公交在 x 时刻出发，满足 y <= x  且公交没有满，那么你可以搭乘这一辆公交。
# 最早 到达的乘客优先上车。
# 返回你可以搭乘公交车的最晚到达公交站时间。你 不能 跟别的乘客同时刻到达。

# 注意：数组 buses 和 passengers 不一定是有序的。

# 示例 1：
# 输入：buses = [10,20], passengers = [2,17,18,19], capacity = 2
# 输出：16
# 解释：
# 第 1 辆公交车载着第 1 位乘客。
# 第 2 辆公交车载着你和第 2 位乘客。
# 注意你不能跟其他乘客同一时间到达，所以你必须在第二位乘客之前到达。
# 示例 2：
# 输入：buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2
# 输出：20
# 解释：
# 第 1 辆公交车载着第 4 位乘客。
# 第 2 辆公交车载着第 6 位和第 2 位乘客。
# 第 3 辆公交车载着第 1 位乘客和你。

# 提示：
# n == buses.length
# m == passengers.length
# 1 <= n, m, capacity <= 105
# 2 <= buses[i], passengers[i] <= 109
# buses 中的元素 互不相同 。
# passengers 中的元素 互不相同 。


class Solution:

    def latestTimeCatchTheBus(self, buses: list[int], passengers: list[int], capacity):
        """二分答案法：代码正确 但 超时"""
        n, m = len(buses), len(passengers)
        buses.sort()
        passengers.sort()
        l, r = 0, max(buses)

        def check(t):
            """你在t时间点到达车站，返回你能不能坐到公交车（先不管 "你不能跟别的乘客同时刻到达" 这个条件 ）"""
            temp = passengers[:]
            if t <= temp[0]:
                temp.insert(0, t)
            elif t > temp[-1]:
                temp.append(t)
            else:
                for i in range(m - 1):
                    if temp[i] < t <= temp[i + 1]:
                        temp.insert(i + 1, t)
            i, j = 0, 0
            people = 0
            while j < m + 1:
                if i >= n:
                    return False
                if temp[j] <= buses[i] and people < capacity:
                    if temp[j] == t:
                        return True
                    people += 1
                    j += 1
                else:
                    people = 0
                    i += 1
            return False

        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        while ans in (p := set(passengers)):
            ans -= 1
        return ans

    def latestTimeCatchTheBus(self, buses: list[int], passengers: list[int], capacity):
        # 贪心就完事了！
        # * 上帝视角：你可以插队
        # * 找到最后一个上车的人，那么他前面的人也一定上车了！
        # * 顺着最后一个人往前找，找到一个空位进行插队，就是答案。
        buses.sort()
        passengers.sort()
        n = len(passengers)
        j = 0
        # 双指针
        for t in buses:
            c = capacity
            while c > 0 and j < n and passengers[j] <= t:
                c -= 1
                j += 1
        j -= 1
        ans = buses[-1] if c > 0 else passengers[j]
        while j >= 0 and passengers[j] == ans:
            ans -= 1
            j -= 1
        return ans


if __name__ == "__main__":
    s = Solution()
    buses = [10, 20]
    passengers = [2, 17, 18, 19]
    capacity = 2
    print(s.latestTimeCatchTheBus(buses, passengers, capacity))
