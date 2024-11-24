#
# * 907. 子数组的最小值之和 - M
# 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
# 由于答案可能很大，因此 返回答案模 10^9 + 7 。

# 示例 1：
# 输入：arr = [3,1,2,4]
# 输出：17
# 解释：
# 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
# 示例 2：
# 输入：arr = [11,81,94,43,3]
# 输出：444

# 提示：
# 1 <= arr.length <= 3 * 10^4
# 1 <= arr[i] <= 3 * 10^4


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        """以 arr[i] 为最小值的子数组的个数为 (i−L)⋅(R−i)，对答案的贡献为 arr[i]⋅(i−L)⋅(R−i)。"""

        """注意：修改边界定义，避免重复统计子数组
        如果 arr 有重复元素，例如 arr=[1,2,4,2,3,1]，其中第一个 2 和第二个 2 对应的边界都是开区间 (0,5)，子数组 [2,4,2,3] 都包含这两个 2，
        这样在计算答案时就会重复统计同一个子数组，算出错误的结果。

        为避免重复统计，可以修改边界的定义，把右边界改为「找小于或等于 arr[i] 的数的下标」，那么：

        第一个 2 对应的边界是 (0,3)，子数组需要在 (0,3) 范围内且包含下标 1；
        第二个 2 对应的边界是 (0,5)，子数组需要在 (0,5) 范围内且包含下标 3。
        这样以第一个 2 为最小值的子数组，就不会「越界」包含第二个 2 了，从而解决了重复统计子数组的问题。

        注：也可以把左边界改为 ≤，右边界不变（仍为 <）。根据对称性，算出来的答案是一样的。"""
        n = len(arr)
        left = [-1] * n  # 左边小于等于当前数，且最近的数
        right = [n] * n  # 右边严格小于当前数，且最近的数
        stack = []
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] >= num:
                right[stack.pop()] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        # stack = []
        # 注释这么做会重复计算
        # for i in range(n - 1, -1, -1):
        #     while stack and arr[stack[-1]] > arr[i]:
        #         left[stack.pop()] = i
        #     stack.append(i)

        # ans = 0
        # for i in range(n):
        #     # 以每个位置为最小值子数组的个数 * 当前值
        #     ans = (ans + arr[i] * (i - left[i]) * (right[i] - i)) % (10**9 + 7)
        # return ans % (10**9 + 7)

        ans = 0
        for i, (x, l, r) in enumerate(zip(arr, left, right)):
            ans += x * (i - l) * (r - i)  # 累加贡献
        return ans % (10**9 + 7)


if __name__ == "__main__":
    sol = Solution()
    arr = [3, 1, 2, 4]
    print(sol.sumSubarrayMins(arr))
