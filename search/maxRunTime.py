#
# * 2141. 同时运行 N 台电脑的最长时间 - H
# 你有 n 台电脑。给你整数 n 和一个下标从 0 开始的整数数组 batteries ，其中第 i 个电池可以让一台电脑 运行 batteries[i] 分钟。你想使用这些电池让 全部 n 台电脑 同时 运行。
# 一开始，你可以给每台电脑连接 至多一个电池 。然后在任意整数时刻，你都可以将一台电脑与它的电池断开连接，并连接另一个电池，你可以进行这个操作 任意次 。新连接的电池可以是一个全新的电池，也可以是别的电脑用过的电池。断开连接和连接新的电池不会花费任何时间。
# 注意，你不能给电池充电。
# 请你返回你可以让 n 台电脑同时运行的 最长 分钟数。

# 示例 1：
# 输入：n = 2, batteries = [3,3,3]
# 输出：4
# 解释：
# 一开始，将第一台电脑与电池 0 连接，第二台电脑与电池 1 连接。
# 2 分钟后，将第二台电脑与电池 1 断开连接，并连接电池 2 。注意，电池 0 还可以供电 1 分钟。
# 在第 3 分钟结尾，你需要将第一台电脑与电池 0 断开连接，然后连接电池 1 。
# 在第 4 分钟结尾，电池 1 也被耗尽，第一台电脑无法继续运行。
# 我们最多能同时让两台电脑同时运行 4 分钟，所以我们返回 4 。


class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:

        def check(time):
            """确定每台电脑的运行时间，返回使用这些电池能不达成目标"""
            t = n
            Fragments_sum = 0  # 碎片电量总和
            for b in batteries:
                if b >= time:
                    t -= 1
                else:
                    Fragments_sum += b
                if Fragments_sum >= t * time:
                    return True
            return False

        sum_ = sum(batteries)
        max_ = max(batteries)
        if sum_ > max_ * n:
            # 所有电池的最大电量是max
            # 如果此时sum > (long) max * num，
            # 说明 : 最终的供电时间一定在 >= max，而如果最终的供电时间 >= max
            # 说明 : 对于最终的答案X来说，所有电池都是课上讲的"碎片拼接"的概念
            # 那么寻找 ? * num <= sum 的情况中，尽量大的 ? 即可
            # 即sum / num
            return sum_ // n

        l, r = 0, max_
        while l <= r:  # 必须有等于号
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r

    def maxRunTime2(self, n: int, batteries: list[int]) -> int:
        """那么要让 n 台电脑同时运行 x 分钟，充分必要条件是 n*x ≤ sum"""
        """二分答案"""
        l, r = 0, sum(batteries) // n
        while l < r:
            x = (l + r + 1) // 2
            if n * x <= sum(min(b, x) for b in batteries):
                l = x
            else:
                r = x - 1
        return l

    def maxRunTime3(self, n: int, batteries: list[int]) -> int:
        """排序 + 贪心"""
        batteries.sort(reverse=True)
        s = sum(batteries)
        for b in batteries:
            if b <= s // n:
                return s // n
            s -= b
            n -= 1


if __name__ == "__main__":
    sol = Solution()
    n = 2
    batteries = [3, 3, 3]
    print(sol.maxRunTime(n, batteries))
    print(sol.maxRunTime2(n, batteries))
    print(sol.maxRunTime3(n, batteries))
