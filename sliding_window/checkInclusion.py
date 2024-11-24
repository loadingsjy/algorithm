# 字符串的排列
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
# 换句话说，s1 的排列之一是 s2 的 子串 。

# 示例 1：
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
# 示例 2：
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        left = 0
        n = len(s2)
        cnt_s1 = Counter(s1)
        cnt_s2 = Counter()

        for right in range(n):
            cnt_s2[s2[right]] += 1
            if cnt_s1 == cnt_s2:
                return True
            while cnt_s2 > cnt_s1:
                cnt_s2[s2[left]] -= 1
                left += 1

                if cnt_s1 == cnt_s2:
                    return True
        return False

    def checkInclusion2(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        cnt_s1 = Counter(s1)
        cnt_s2 = Counter(s2[:n1])
        if cnt_s1 == cnt_s2:
            return True
        for i in range(1, n2 - n1 + 1):
            cnt_s2[s2[i - 1]] -= 1
            cnt_s2[s2[i + n1 - 1]] += 1
            if cnt_s2 == cnt_s1:
                return True
        return False

    def checkInclusion3(self, s1: str, s2: str) -> bool:
        """
        思路：怎么判断s2的字串和s1的排列之一相等，假如排序的话，遍历s2的同时，每次都排序，总的时间复杂度太高了。
        因此，我们采用一个有序字典来比较，由于只包含小写字母，我们采用数组来模拟有序字典，
        这样判断s2的子串和s1的排列之一相等就很容易了。总的时间复杂度为O(n),n为s2的长度。
        空间复杂度为:O(26)*2 == O(1)

        """
        m1 = len(s1)
        m2 = len(s2)
        if m1 > m2:
            return False
        dic1 = [0] * 26
        dic2 = [0] * 26
        for i in range(m1):
            dic1[ord(s1[i]) - ord("a")] += 1
            dic2[ord(s2[i]) - ord("a")] += 1
        if dic1 == dic2:
            return True

        for i in range(m1, m2):
            dic2[ord(s2[i - m1]) - ord("a")] -= 1
            dic2[ord(s2[i]) - ord("a")] += 1
            if dic1 == dic2:
                return True
        return False


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    s = Solution()
    print(s.checkInclusion(s1, s2))
    print(s.checkInclusion2(s1, s2))
    print(s.checkInclusion3(s1, s2))
