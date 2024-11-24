#
# * 1870. 准时到达的列车最小时速 - M
# 给你一个浮点数 hour ，表示你到达办公室可用的总通勤时间。要到达办公室，你必须按给定次序乘坐 n 趟列车。另给你一个长度为 n 的整数数组 dist ，其中 dist[i] 表示第 i 趟列车的行驶距离（单位是千米）。
# 每趟列车均只能在整点发车，所以你可能需要在两趟列车之间等待一段时间。
# 例如，第 1 趟列车需要 1.5 小时，那你必须再等待 0.5 小时，搭乘在第 2 小时发车的第 2 趟列车。
# 返回能满足你准时到达办公室所要求全部列车的 最小正整数 时速（单位：千米每小时），如果无法准时到达，则返回 -1 。
# 生成的测试用例保证答案不超过 107 ，且 hour 的 小数点后最多存在两位数字 。

# 示例 1：
# 输入：dist = [1,3,2], hour = 6
# 输出：1
# 解释：速度为 1 时：
# - 第 1 趟列车运行需要 1/1 = 1 小时。
# - 由于是在整数时间到达，可以立即换乘在第 1 小时发车的列车。第 2 趟列车运行需要 3/1 = 3 小时。
# - 由于是在整数时间到达，可以立即换乘在第 4 小时发车的列车。第 3 趟列车运行需要 2/1 = 2 小时。
# - 你将会恰好在第 6 小时到达。
# 示例 2：
# 输入：dist = [1,3,2], hour = 2.7
# 输出：3
# 解释：速度为 3 时：
# - 第 1 趟列车运行需要 1/3 = 0.33333 小时。
# - 由于不是在整数时间到达，故需要等待至第 1 小时才能搭乘列车。第 2 趟列车运行需要 3/3 = 1 小时。
# - 由于是在整数时间到达，可以立即换乘在第 2 小时发车的列车。第 3 趟列车运行需要 2/3 = 0.66667 小时。
# - 你将会在第 2.66667 小时到达。
# 示例 3：
# 输入：dist = [1,3,2], hour = 1.9
# 输出：-1
# 解释：不可能准时到达，因为第 3 趟列车最早是在第 2 小时发车。

# 提示：
# n == dist.length
# 1 <= n <= 105
# 1 <= dist[i] <= 105
# 1 <= hour <= 109
# hours 中，小数点后最多存在两位数字
import math


class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        # 时间必须要大于路程段数减 1
        if hour <= len(dist) - 1:
            return -1

        def using_time(speed):
            """给定速度，返回到达办公室所需要的时间"""
            total = 0
            for distance in dist[:-1]:
                total += math.ceil(distance / speed)
            return total + dist[-1] / speed

        fractional_part, _ = math.modf(hour)

        l = 1
        r = (
            max(dist)
            if fractional_part == 0
            else max(max(dist), math.ceil(dist[-1] / fractional_part))
        )
        while l <= r:
            mid = (l + r) // 2
            if using_time(mid) <= hour:
                r = mid - 1
            else:
                l = mid + 1
        return l

    def minSpeedOnTime2(self, dist: list[int], hour: float) -> int:
        """官方答案"""
        n = len(dist)
        hr = round(hour * 100)
        # 时间必须要大于路程段数减 1
        if hr <= 100 * (n - 1):
            return -1

        # 判断当前时速是否满足时限
        def check(speed: int) -> bool:
            t = 0
            # 前 n-1 段中第 i 段贡献的时间： floor(dist[i] / mid)
            for i in range(n - 1):
                t += (dist[i] - 1) // speed + 1
            # 最后一段贡献的时间： dist[n-1] / mid
            t *= speed
            t += dist[-1]
            return t * 100 <= hr * speed  # 通分以转化为整数比较

        # 二分
        l, r = 1, 10**7
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l  # 满足条件的最小时速

    def minSpeedOnTime3(self, dist: list[int], hour: float) -> int:
        """避免浮点运算的写法，由于 hour 至多有两位小数，不妨将其乘上 100，视作整数"""
        n = len(dist)
        h100 = round(hour * 100)
        # h100 = hour * 100  # 这个得出的结果是200.99999999999997，所以不能用int，只能用round
        # h100 = int(h100)
        if h100 <= (n - 1) * 100:  # hour 必须严格大于 n-1
            return -1

        def check(speed):
            """给定速度，返回到达办公室所需要的时间"""
            total = 0
            for distance in dist[:-1]:
                total += math.ceil(distance / speed)
            return (total * speed + dist[-1]) * 100 <= h100 * speed

        l = 1
        r = 1e7
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return math.ceil(l)

    def minSpeedOnTime4(self, dist: list[int], hour: float) -> int:
        """最优版本"""
        n = len(dist)
        m = max(dist)
        # 如果小于n - 1，一定无法按时到达
        if hour <= n - 1:
            return -1
        # 如果尾数很小，则要以超快速运行
        if hour < n:
            return max(m, round(dist[-1] / (hour - n + 1)))
        # 时速最慢1，最快max
        left = 1
        right = m
        while left <= right:
            mid = (left + right) // 2
            # 满足条件，速度可以降低
            if sum(math.ceil(d / mid) for d in dist[:-1]) + dist[-1] / mid <= hour:
                right = mid - 1
            else:
                left = mid + 1
        return right + 1


if __name__ == "__main__":
    sol = Solution()
    dist = [1, 1, 100000]
    hour = 2.01
    print(sol.minSpeedOnTime(dist, hour))
    print(sol.minSpeedOnTime2(dist, hour))
    print(sol.minSpeedOnTime3(dist, hour))
    print(sol.minSpeedOnTime4(dist, hour))
    print()

    dist = [1, 3, 2]
    hour = 6
    print(sol.minSpeedOnTime(dist, hour))
    print(sol.minSpeedOnTime2(dist, hour))
    print(sol.minSpeedOnTime3(dist, hour))
    print(sol.minSpeedOnTime4(dist, hour))
