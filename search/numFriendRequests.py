#
# * 825. 适龄的朋友
# 在社交媒体网站上有 n 个用户。给你一个整数数组 ages ，其中 ages[i] 是第 i 个用户的年龄。
# 如果下述任意一个条件为真，那么用户 x 将不会向用户 y（x != y）发送好友请求：
# ages[y] <= 0.5 * ages[x] + 7
# ages[y] > ages[x]
# ages[y] > 100 && ages[x] < 100
# 否则，x 将会向 y 发送一条好友请求。
# 注意，如果 x 向 y 发送一条好友请求，y 不必也向 x 发送一条好友请求。另外，用户不会向自己发送好友请求。
# 返回在该社交媒体网站上产生的好友请求总数。
# 示例 1：
# 输入：ages = [16,16]
# 输出：2
# 解释：2 人互发好友请求。
# 示例 2：
# 输入：ages = [16,17,18]
# 输出：2
# 解释：产生的好友请求为 17 -> 16 ，18 -> 17 。
# 示例 3：
# 输入：ages = [20,30,100,110,120]
# 输出：3
# 解释：产生的好友请求为 110 -> 100 ，120 -> 110 ，120 -> 100 。
# 提示：
# n == ages.length
# 1 <= n <= 2 * 104
# 1 <= ages[i] <= 120

from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        n = len(ages)
        ages.sort()
        start = bisect_right(ages, 14)  # 由前两个条件可知x一定大于14
        ans = 0
        i = start
        while i < n:    # 对于每个x找到满足y<=x and y > 0.5x + 1 的位置
            x = ages[i]
            j = i
            while j + 1 < n and ages[j + 1] == ages[j]:
                j += 1
            ans += (j - i + 1) * (j - i)
            ans += (i - bisect_right(ages, x / 2 + 7, 0, i)) * (j - i + 1)
            i = j + 1
        return ans

    def numFriendRequests(self, ages: List[int]) -> int:
        """
        由于 n 很大而 ages[i]≤120，我们可以用一个长为 121 的 cnt 数组统计每个年龄的人数。

        枚举年龄 ageX，我们需要知道：
        可以发送好友请求的最小年龄 ageY 是多少。
        年龄在区间 [ageY,ageX] 中的人数。
        由于 ageX 越大，ageY 也越大，可以用滑动窗口解决。
        窗口内维护年龄在区间 [ageY,ageX] 中的人数 cntWindow。

        如果发现 cntWindow>0，说明存在可以发送好友请求的用户：
        当前这 cnt[ageX] 个用户可以与 cntWindow 个用户发送好友请求，根据乘法原理，这有 cnt[ageX]⋅cntWindow 个。
        其中有 cnt[ageX] 个好友请求是自己发给自己的，不符合题目要求，要减去。
        所以把cnt[ageX]⋅cntWindow−cnt[ageX]加入答案。
        
        时间复杂度：O(n+U)，其中 n 是 ages 的长度，U=max(ages) ≤ 120。
        空间复杂度：O(U)。
        """
        cnt = [0] * 121
        for age in ages:
            cnt[age] += 1

        ans = cnt_window = age_y = 0
        for age_x, c in enumerate(cnt):
            cnt_window += c
            if age_y * 2 <= age_x + 14:  # 不能发送好友请求
                cnt_window -= cnt[age_y]
                age_y += 1
            if cnt_window:  # 存在可以发送好友请求的用户
                ans += c * cnt_window - c
        return ans


if __name__ == "__main__":
    sol = Solution()
    ages = [16, 16]
    print(sol.numFriendRequests(ages))
