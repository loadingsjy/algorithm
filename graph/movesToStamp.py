#
# * 936. 戳印序列 - H
# 你想要用小写字母组成一个目标字符串 target。
# 开始的时候，序列由 target.length 个 '?' 记号组成。而你有一个小写字母印章 stamp。
# 在每个回合，你可以将印章放在序列上，并将序列中的每个字母替换为印章上的相应字母。你最多可以进行 10 * target.length  个回合。
# 举个例子，如果初始序列为 "?????"，而你的印章 stamp 是 "abc"，那么在第一回合，你可以得到 "abc??"、"?abc?"、"??abc"。
# （请注意，印章必须完全包含在序列的边界内才能盖下去。）
# 如果可以印出序列，那么返回一个数组，该数组由每个回合中被印下的最左边字母的索引组成。如果不能印出序列，就返回一个空数组。
# 例如，如果序列是 "ababc"，印章是 "abc"，那么我们就可以返回与操作 "?????" -> "abc??" -> "ababc" 相对应的答案 [0, 2]；
# 另外，如果可以印出序列，那么需要保证可以在 10 * target.length 个回合内完成。任何超过此数字的答案将不被接受。

# 示例 1：
# 输入：stamp = "abc", target = "ababc"
# 输出：[0,2]
# （[1,0,2] 以及其他一些可能的结果也将作为答案被接受）
# 示例 2：
# 输入：stamp = "abca", target = "aabcaca"
# 输出：[3,0,1]

# 提示：
# 1 <= stamp.length <= target.length <= 1000
# stamp 和 target 只包含小写字母。
from collections import defaultdict


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        """时光倒流 + 拓扑排序   最后盖上的可以修改之前的错误"""
        n, m = len(target), len(stamp)
        # key: 有错误的位置 value: 属于以哪个位置开头的范围的
        next_nodes = defaultdict(list)
        in_degree = [m] * (n - m + 1)  # 以i为开头的产生的错误数量
        queue = []
        for i in range(n - m + 1):
            for j in range(m):
                if stamp[j] == target[i + j]:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        queue.append(i)
                else:
                    next_nodes[i + j].append(i)
        # 同一个位置的错误不要重复统计
        visited = [False] * n
        ans = []
        while queue:
            cur = queue.pop(0)
            ans.append(cur)
            for i in range(cur, cur + m):
                if not visited[i]:
                    visited[i] = True
                    for start in next_nodes[i]:
                        in_degree[start] -= 1
                        if in_degree[start] == 0:
                            queue.append(start)
        if len(ans) != n - m + 1:
            return []
        return ans[::-1]


if __name__ == "__main__":
    sol = Solution()
    stamp = "abca"
    target = "aabcaca"
    print(sol.movesToStamp(stamp, target))
