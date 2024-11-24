#
# * 605. 种花问题 - E
# 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
# 给你一个整数数组 flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。
# 另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false 。

# 示例 1：
# 输入：flowerbed = [1,0,0,0,1], n = 1
# 输出：true
# 示例 2：
# 输入：flowerbed = [1,0,0,0,1], n = 2
# 输出：false

# 提示：
# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] 为 0 或 1
# flowerbed 中不存在相邻的两朵花
# 0 <= n <= flowerbed.length


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        length = 0
        ans = 0
        for num in [0] + flowerbed + [0]:
            if num == 0:
                length += 1
            else:
                ans += int((length - 1) / 2)
                length = 0
        ans += int((length - 1) / 2)
        return ans >= n

    def canPlaceFlowers2(self, flowerbed: list[int], n: int) -> bool:
        """
        如何判断能否种花？由于「花不能种植在相邻的地块上」，如果要在下标 i 处种花，需要满足 flowerbed[i−1],flowerbed[i],flowerbed[i+1] 均为 0。
        每种一朵花，就把 n 减一。如果最后 n≤0，则返回 true，否则返回 false。
        为了简化判断逻辑，可以在数组的开头和末尾各插入一个 0。
        """
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1  # 种花！
                n -= 1
        return n <= 0

    def canPlaceFlowers3(self, flowerbed: list[int], n: int) -> bool:
        i, m = 0, len(flowerbed)
        while i < m:
            if (
                (i == 0 or flowerbed[i - 1] == 0)
                and flowerbed[i] == 0
                and (i == m - 1 or flowerbed[i + 1] == 0)
            ):
                n -= 1
                i += 2  # 下一个位置肯定不能种花，直接跳过
            else:
                i += 1
        return n <= 0


if __name__ == "__main__":
    sol = Solution()
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(sol.canPlaceFlowers(flowerbed, n))
    print(sol.canPlaceFlowers2(flowerbed, n))
    print(sol.canPlaceFlowers3(flowerbed, n))
