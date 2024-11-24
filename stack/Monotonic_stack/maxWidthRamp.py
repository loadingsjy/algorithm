#
# * 962. 最大宽度坡 -  M
# 给定一个整数数组 A，坡是元组 (i, j)，其中  i < j 且 A[i] <= A[j]。这样的坡的宽度为 j - i。
# 找出 A 中的坡的最大宽度，如果不存在，返回 0 。

# 示例 1：
# 输入：[6,0,8,2,1,5]
# 输出：4
# 解释：
# 最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.
# 示例 2：
# 输入：[9,8,1,0,1,9,4,0,4,1]
# 输出：7
# 解释：
# 最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.

# 提示：
# 2 <= A.length <= 50000
# 0 <= A[i] <= 50000


class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        n = len(nums)
        stack = [0]
        # 得到右侧答案的最优可能性
        for i in range(1, n):
            if nums[i] < nums[stack[-1]]:
                stack.append(i)
        ans = 0
        # 反向遍历，和栈顶元素比较得出最长坡度
        for i in range(n - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                ans = max(ans, i - stack.pop())
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [6, 0, 8, 2, 1, 5]
    print(sol.maxWidthRamp(nums))
