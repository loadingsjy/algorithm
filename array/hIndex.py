# 274. H 指数
# 给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。
# 根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，并且 至少 有 h 篇论文被引用次数大于等于 h 。
# 如果 h 有多种可能的值，h 指数 是其中最大的那个。

# 示例 1：
# 输入：citations = [3,0,6,1,5]
# 输出：3
# 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
#      由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
# 示例 2：
# 输入：citations = [1,3,1]
# 输出：1


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """时间复杂度O(n)，O(nlogn)"""
        citations.sort()
        n = len(citations)
        ans = 0
        for i in range(n):
            # 当前最少的引用次数 >= 比该引用次数多的文章有n-i个
            if citations[i] >= n - i:
                ans = max(ans, n - i)
        return ans

    def hIndex2(self, citations: list[int]) -> int:
        """新建并维护一个数组 counter 用来记录当前引用次数的论文有几篇。时间复杂度O(n)"""
        n = len(citations)
        tot = 0
        counter = [0] * (n + 1)
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1
        for i in range(n, -1, -1):
            tot += counter[i]
            if tot >= i:
                return i
        return 0


if __name__ == "__main__":
    s = Solution()
    citations = [3, 0, 6, 1, 5]
    print(s.hIndex(citations))
    print(s.hIndex2(citations))
