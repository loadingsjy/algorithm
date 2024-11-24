# 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。

# 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
# 返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。


# 示例 1：
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：[0,1]
# 解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
# 示例 2：
# 输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# 输出：[0,2,1,3]
# 解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
# 因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
# 示例 3：
# 输入：numCourses = 1, prerequisites = []
# 输出：[0]
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        if not prerequisites:
            return list(range(numCourses))

        next_dict = collections.defaultdict(list)  # key:节点id  value:邻节点列表
        in_degree_dict = collections.defaultdict(int)
        all_courses = list(range(numCourses))

        for i, j in prerequisites:
            in_degree_dict[i] += 1
            next_dict[j].append(i)

        ans = []
        while all_courses:
            last_l = len(all_courses)
            for idx in all_courses:
                if in_degree_dict[idx] == 0:
                    ans.append(idx)
                    all_courses.remove(idx)
                    for course in next_dict[idx]:
                        in_degree_dict[course] -= 1
            if last_l == len(all_courses):
                break
        if len(all_courses) != 0:
            return []
        return ans

    def findOrder2(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """广度优先搜索 + 拓扑排序"""
        if not prerequisites:
            return list(range(numCourses))

        # 存储有向图
        edges = collections.defaultdict(list)
        # 存储每个节点的入度
        in_degree_dict = collections.defaultdict(int)
        for i, j in prerequisites:
            edges[j].append(i)
            in_degree_dict[i] += 1

        ans = []
        queue = []

        for idx in range(numCourses):
            if in_degree_dict[idx] == 0:
                queue.append(idx)

        while queue:
            t = queue.pop(0)
            ans.append(t)
            for v in edges[t]:
                in_degree_dict[v] -= 1
                # 如果相邻节点 v 的入度为 0，就可以选 v 对应的课程了
                if in_degree_dict[v] == 0:
                    queue.append(v)

        if len(ans) != numCourses:
            return []
        else:
            return ans
