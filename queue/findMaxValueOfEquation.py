#
# * 1499. 满足不等式的最大值 - H
# 给你一个数组 points 和一个整数 k 。数组中每个元素都表示二维平面上的点的坐标，并按照横坐标 x 的值从小到大排序。也就是说 points[i] = [xi, yi] ，并且在 1 <= i < j <= points.length 的前提下， xi < xj 总成立。
# 请你找出 yi + yj + |xi - xj| 的 最大值，其中 |xi - xj| <= k 且 1 <= i < j <= points.length。
# 题目测试数据保证至少存在一对能够满足 |xi - xj| <= k 的点。

# 示例 1：
# 输入：points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
# 输出：4
# 解释：前两个点满足 |xi - xj| <= 1 ，代入方程计算，则得到值 3 + 0 + |1 - 2| = 4 。第三个和第四个点也满足条件，得到值 10 + -10 + |5 - 6| = 1 。
# 没有其他满足条件的点，所以返回 4 和 1 中最大的那个。
# 示例 2：
# 输入：points = [[0,0],[3,0],[9,2]], k = 3
# 输出：3
# 解释：只有前两个点满足 |xi - xj| <= 3 ，代入方程后得到值 0 + 0 + |0 - 3| = 3 。

# 提示：
# 2 <= points.length <= 10^5
# points[i].length == 2
# -10^8 <= points[i][0], points[i][1] <= 10^8
# 0 <= k <= 2 * 10^8
# 对于所有的1 <= i < j <= points.length ，points[i][0] < points[j][0] 都成立。也就是说，xi 是严格递增的。

from collections import deque


class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        """yi + yj + |xi - xj| = (yi - xi) + (xj + yj)，求|xi-xj|<=k的条件下(yi - xi)的最大值"""
        Maxq = deque()

        ans = float("-inf")
        for right, (x, y) in enumerate(points):
            while Maxq and x - points[Maxq[0]][0] > k:  # x与头部的横坐标距离超过了k
                Maxq.popleft()
            if Maxq:
                ans = max(ans, x + y + points[Maxq[0]][1] - points[Maxq[0]][0])

            while Maxq and y - x >= points[Maxq[-1]][1] - points[Maxq[-1]][0]:
                Maxq.pop()

            Maxq.append(right)
        return ans

    def findMaxValueOfEquation2(self, points: list[list[int]], k: int) -> int:
        """灵神写法：
        枚举 j，问题变成计算 yi​−xi的最大值，其中 i<j 且 xi≥xj−k。
        用单调队列优化：
        1.单调队列存储二元组 (xi,yi−xi)。
        2.首先把队首的超出范围的数据出队，即 xi<xj−k 的数据。
        3.然后把 (xj,yj−xj​) 入队，入队前如果发现 yj−xj不低于队尾的数据，那么直接弹出队尾。
        4.这样维护后，单调队列的 yi​−xi​从队首到队尾是严格递减的，yi−xi的最大值即为队首的最大值。
        形象一点的说法是，老员工的能力必须比新来的强。否则就淘汰"""
        ans = float("-inf")
        q = deque()
        for x, y in points:
            while q and q[0][0] < x - k:  # 队首超出范围
                q.popleft()  # 弹它！
            if q:
                ans = max(ans, x + y + q[0][1])  # 加上最大的 yi-xi
            while q and q[-1][1] <= y - x:  # 队尾不如新来的强
                q.pop()  # 弹它！
            q.append((x, y - x))
        return ans


if __name__ == "__main__":
    sol = Solution()
    points = [[1, 3], [2, 0], [5, 10], [6, -10]]
    k = 1
    print(sol.findMaxValueOfEquation(points, k))
    print(sol.findMaxValueOfEquation2(points, k))
