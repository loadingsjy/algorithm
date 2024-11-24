#
# * 1151. 最少交换次数来组合所有的 1 - M
# 给出一个二进制数组 data，你需要通过交换位置，将数组中 任何位置 上的 1 组合到一起，并返回所有可能中所需 最少的交换次数。


# 示例 1:
# 输入: data = [1,0,1,0,1]
# 输出: 1
# 解释:
# 有三种可能的方法可以把所有的 1 组合在一起：
# [1,1,1,0,0]，交换 1 次；
# [0,1,1,1,0]，交换 2 次；
# [0,0,1,1,1]，交换 1 次。
# 所以最少的交换次数为 1。
# 示例  2:
# 输入：data = [0,0,0,1,0]
# 输出：0
# 解释：
# 由于数组中只有一个 1，所以不需要交换。
# 示例 3:
# 输入：data = [1,0,1,0,1,0,0,1,1,0,1]
# 输出：3
# 解释：
# 交换 3 次，一种可行的只用 3 次交换的解决方案是 [0,0,0,0,0,1,1,1,1,1,1]。
# 示例 4:
# 输入: data = [1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]
# 输出: 8

# 提示:
# 1 <= data.length <= 105
# data[i] == 0 or 1.


class Solution:
    def minSwaps(self, data: list[int]) -> int:
        n = len(data)
        window = sum(data)  # 窗口大小，必须容纳所有的1
        count_0 = 0  # 窗口内0的个数就是至少要交换的次数
        for i in range(window):
            if data[i] == 0:
                count_0 += 1
        ans = count_0
        for i in range(window, n):
            count_0 += data[i] == 0
            count_0 -= data[i - window] == 0
            ans = min(ans, count_0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    data = [1, 0, 1, 0, 1]
    print(sol.minSwaps(data))
