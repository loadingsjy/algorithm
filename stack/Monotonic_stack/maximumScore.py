# * 1793. 好子数组的最大分数
# 给你一个整数数组 nums （下标从 0 开始）和一个整数 k 。
# 一个子数组 (i, j) 的 分数 定义为 min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1) 。一个 好 子数组的两个端点下标需要满足 i <= k <= j 。
# 请你返回 好 子数组的最大可能 分数 。

# 示例 1：
# 输入：nums = [1,4,3,7,4,5], k = 3
# 输出：15
# 解释：最优子数组的左右端点下标是 (1, 5) ，分数为 min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15 。
# 示例 2：
# 输入：nums = [5,5,4,5,4,1,1,1], k = 0
# 输出：20
# 解释：最优子数组的左右端点下标是 (0, 4) ，分数为 min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20 。


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left, right = k - 1, k + 1
        ans = 0
        for i in range(nums[k], 0, -1):
            while left >= 0 and nums[left] >= i:
                left -= 1
            while right < n and nums[right] >= i:
                right += 1
            ans = max(ans, (right - left - 1) * i)
        return ans

    def maximumScore2(self, nums: list[int], k: int) -> int:
        """官方答案"""
        n = len(nums)
        left, right, i = k - 1, k + 1, nums[k]
        ans = 0
        while True:
            while left >= 0 and nums[left] >= i:
                left -= 1
            while right < n and nums[right] >= i:
                right += 1
            ans = max(ans, (right - left - 1) * i)
            i = max(
                (-1 if left == -1 else nums[left]), (-1 if right == n else nums[right])
            )
            if i == -1:
                break
        return ans

    def maximumScore3(self, nums: list[int], k: int) -> int:
        """单调栈：栈低放小的元素，栈顶放大的元素，求数组每个数的左/右边最近比它（严格）小的数字的index"""
        n = len(nums)
        pre = [-1] * n
        after = [n] * n
        stack = []
        for i, num in enumerate(nums):
            while stack and num < nums[stack[-1]]:
                after[stack.pop()] = i
            stack.append(i)

        for i in range(n - 1, -1, -1):
            while stack and nums[i] < nums[stack[-1]]:
                pre[stack.pop()] = i
            stack.append(i)

        ans = float("-inf")
        for i in range(n):
            p = pre[i]
            a = after[i]
            if p + 1 <= k <= a - 1:
                ans = max(ans, nums[i] * (a - p - 1))
        return ans


if __name__ == "__main__":

    s = Solution()
    nums = [1, 4, 3, 7, 4, 5]
    k = 3
    print(s.maximumScore(nums, k))
    print(s.maximumScore2(nums, k))
