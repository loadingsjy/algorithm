#
# * 2127. 参加会议的最多员工数 - H
# 一个公司准备组织一场会议，邀请名单上有 n 位员工。
# 公司准备了一张 圆形 的桌子，可以坐下 任意数目 的员工。员工编号为 0 到 n - 1 。
# 每位员工都有一位 喜欢 的员工，每位员工 当且仅当 他被安排在喜欢员工的旁边，他才会参加会议。每位员工喜欢的员工 不会 是他自己。
# 给你一个下标从 0 开始的整数数组 favorite ，其中 favorite[i] 表示第 i 位员工喜欢的员工。请你返回参加会议的 最多员工数目 。

from collections import deque


class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        """内向基环树:
        基环树是指其具有 n 个点 n 条边的联通块，而「内向」是指树中任意节点有且只有一条出边，对应的「外向」是指树中任意节点有且只有一条入边。
        基于拓扑排序 + 动态规划
        1) 小环: 长度为2的环, 两个节点的最长链节点个数(最大深度)之和 + 2
        2) 大环: 长度大于2的环, 环本身的长度, 最后最大环节点数量
        3) 最后答案为以上两种情况的最大值
        """
        n = len(favorite)
        indegree = [0] * n
        for i, j in enumerate(favorite):
            indegree[j] += 1
        queue = deque(i for i in range(n) if indegree[i] == 0)
        # 求每个节点的最大深度（到达它的最长链长度）, 不包括节点本身
        max_deepth = [0] * n
        while queue:
            cur = queue.popleft()
            like = favorite[cur]
            max_deepth[like] = max(max_deepth[like], max_deepth[cur] + 1)
            indegree[like] -= 1
            if indegree[like] == 0:
                queue.append(like)

        sumOfSmallRing = 0  # 小环的答案：中心点个数 + 两个最长延升链的长度
        bigRing = 0  # 大环的答案: 只算中心点个数，最后求最大环的中心点个数
        # 目前图中只剩环了，indegree=0的点都删掉了
        for i in range(n):
            if indegree[i] == 0:
                continue
            ringSize = 1
            indegree[i] = 0
            j = favorite[i]
            while j != i:
                ringSize += 1
                indegree[j] = 0
                j = favorite[j]
            if ringSize == 2:
                sumOfSmallRing += 2 + max_deepth[i] + max_deepth[favorite[i]]
            else:
                bigRing = max(bigRing, ringSize)
        return max(sumOfSmallRing, bigRing)


if __name__ == "__main__":
    sol = Solution()
    favorite = [1, 0, 0, 2, 1, 4, 7, 8, 9, 6, 7, 10, 8]
    print(sol.maximumInvitations(favorite))
