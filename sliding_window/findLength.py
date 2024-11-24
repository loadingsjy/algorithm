# * 最长重复子数组
# 给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。
# 示例 1：
# 输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# 输出：3
# 解释：长度最长的公共子数组是 [3,2,1] 。
# 示例 2：
# 输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# 输出：5


class Solution:
    def findLength(self, nums1, nums2) -> int:
        def maxLength(addA: int, addB: int, length: int) -> int:
            """addA为nums1的起始索引，addB为nums2的起始索引，lenght为公共长度"""
            ret = k = 0
            for i in range(length):
                if nums1[addA + i] == nums2[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret

        n, m = len(nums1), len(nums2)
        ret = 0
        # 枚举nums1和nums2的所有的对齐方式
        for i in range(n):
            length = min(m, n - i)
            ret = max(ret, maxLength(i, 0, length))
        for i in range(m):
            length = min(n, m - i)
            ret = max(ret, maxLength(0, i, length))
        return ret

    def findLength_dp(self, nums1, nums2) -> int:
        """令 dp[i][j] 表示 A[i:] 和 B[j:](必须包含i和j) 的最长公共前缀，那么答案即为所有 dp[i][j] 中的最大值。
        如果 A[i] == B[j]，那么 dp[i][j] = dp[i + 1][j + 1] + 1，否则 dp[i][j] = 0。"""
        n, m = len(nums1), len(nums1)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if nums1[i] == nums2[j] else 0
                ans = max(ans, dp[i][j])
        return ans


if __name__ == "__main__":
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]
    s = Solution()
    print(s.findLength(nums1, nums2))
    print(s.findLength_dp(nums1, nums2))
