#
# * 1642. 可以到达的最远建筑 - M

# 给你一个整数数组 heights ，表示建筑物的高度。另有一些砖块 bricks 和梯子 ladders 。
# 你从建筑物 0 开始旅程，不断向后面的建筑物移动，期间可能会用到砖块或梯子。
# 当从建筑物 i 移动到建筑物 i+1（下标 从 0 开始 ）时：
# 如果当前建筑物的高度 大于或等于 下一建筑物的高度，则不需要梯子或砖块
# 如果当前建筑的高度 小于 下一个建筑的高度，您可以使用 一架梯子 或 (h[i+1] - h[i]) 个砖块
# 如果以最佳方式使用给定的梯子和砖块，返回你可以到达的最远建筑物的下标（下标 从 0 开始 ）。

# 示例 1：
# 输入：heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
# 输出：4
# 解释：从建筑物 0 出发，你可以按此方案完成旅程：
# - 不使用砖块或梯子到达建筑物 1 ，因为 4 >= 2
# - 使用 5 个砖块到达建筑物 2 。你必须使用砖块或梯子，因为 2 < 7
# - 不使用砖块或梯子到达建筑物 3 ，因为 7 >= 6
# - 使用唯一的梯子到达建筑物 4 。你必须使用砖块或梯子，因为 6 < 9
# 无法越过建筑物 4 ，因为没有更多砖块或梯子。
# 示例 2：
# 输入：heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
# 输出：7
# 示例 3：
# 输入：heights = [14,3,19,3], bricks = 17, ladders = 0
# 输出：3

# 提示：
# 1 <= heights.length <= 105
# 1 <= heights[i] <= 106
# 0 <= bricks <= 109
# 0 <= ladders <= heights.length
import heapq


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        """二分答案法"""
        n = len(heights)
        diff = []
        for i, h in enumerate(heights):
            if i:
                diff.append(h - heights[i - 1])

        def check(idx):
            "返回能否到达 第idx个 建筑物"
            if idx == 0:
                return True
            costs = [d for d in diff[:idx] if d > 0]
            if not costs or len(costs) <= ladders:
                return True
            costs.sort(reverse=True)
            return sum(costs[ladders:]) <= bricks

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r

    def furthestBuilding2(self, heights: list[int], bricks: int, ladders: int) -> int:
        """最优方法：优先队列 + 贪心:
        「梯子」相当于一次性的无限量砖块，那么我们一定是把梯子用在刀刃上。
        也就是说，如果我们有 l 架梯子，那么我们会在 Δh 最大的那 l 次使用梯子，而在剩余的情况下使用砖块。
        这样一来，我们就可以得到正确的算法了：我们使用优先队列实时维护不超过 l 个最大的 Δh，这些就是使用梯子的地方。
        对于剩余的 Δh，我们需要使用砖块，因此需要对它们进行累加，如果某一时刻这个累加值超过了砖块的数目 b，那么我们就再也无法移动了。"""
        n = len(heights)
        # 由于我们需要维护最大的 l 个值，因此使用小根堆
        q = list()
        # 需要使用砖块的 delta h 的和
        sumH = 0
        for i in range(1, n):
            deltaH = heights[i] - heights[i - 1]
            if deltaH > 0:
                heapq.heappush(q, deltaH)
                # 如果优先队列已满，需要拿出一个其中的最小值，改为使用砖块
                if len(q) > ladders:
                    sumH += heapq.heappop(q)
                if sumH > bricks:
                    return i - 1
        return n - 1


if __name__ == "__main__":
    sol = Solution()
    heights = [4, 2, 7, 6, 9, 14, 12]
    bricks = 5
    ladders = 1
    print(sol.furthestBuilding(heights, bricks, ladders))
    print(sol.furthestBuilding2(heights, bricks, ladders))
