#
# * 3208. 交替组 II - M
# 给你一个整数数组 colors 和一个整数 k ，colors表示一个由红色和蓝色瓷砖组成的环，第 i 块瓷砖的颜色为 colors[i] ：
# colors[i] == 0 表示第 i 块瓷砖的颜色是 红色 。
# colors[i] == 1 表示第 i 块瓷砖的颜色是 蓝色 。
# 环中连续 k 块瓷砖的颜色如果是 交替 颜色（也就是说除了第一块和最后一块瓷砖以外，中间瓷砖的颜色与它 左边 和 右边 的颜色都不同），那么它被称为一个 交替 组。
# 请你返回 交替 组的数目。
# 注意 ，由于 colors 表示一个 环 ，第一块 瓷砖和 最后一块 瓷砖是相邻的。

from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        ans, max_length = 0, 0  # max_length 是以i为结尾的最长交替子数组的长度
        for i in range(n + k - 1):
            if i > 0 and colors[i % n] == colors[(i - 1) % n]:
                max_length = 0
            max_length += 1
            if max_length >= k:
                ans += 1
        return ans


if __name__ == "__main__":
    colors = [0, 1, 0, 0, 1, 0, 1]
    k = 6
    print(Solution().numberOfAlternatingGroups(colors, k))
