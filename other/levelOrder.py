# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
# 示例 2：

# 输入：root = [1]
# 输出：[[1]]
# 示例 3：

# 输入：root = []
# 输出：[]

import math
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        n = len(root)
        res = defaultdict(list)

        queue = []
        queue = [(root[0], 1)]
        i = 1
        while queue:
            value, level = queue.pop(0)
            res[level].append(value)

            left_index = 2 * i - 1
            right_index = 2 * i
            level = math.floor(math.log2(left_index + 1)) + 1

            if left_index < n - 1 and root[left_index] != "null":
                queue.append((root[left_index], level))

            if right_index < n and root[right_index] != "null":
                queue.append((root[right_index], level))
            i += 1

        ans = []
        for j in range(1, int(math.log2(n + 1)) + 1):
            ans.append(res[j])
        return ans

    # 有bug
    def list2tree(self, nodes_list):
        """由列表生成二叉树，返回根节点"""
        if not nodes_list:
            return None
        root = TreeNode(val=nodes_list.pop(0))
        q = [root]
        while q:
            t = q.pop(0)
            if nodes_list:
                if nodes_list[0] != "null":
                    t.left = TreeNode(val=nodes_list.pop(0))
                    q.append(t.left)
                else:
                    nodes_list.pop(0)
            if nodes_list:
                if nodes_list[0] != "null":
                    t.right = TreeNode(val=nodes_list.pop(0))
                    q.append(t.right)
                else:
                    nodes_list.pop(0)
        return root

    def levelOrder2(self, root):
        if root is None:
            return []
        else:
            queue = [root]  # 队列先进先出
            res = []
            while queue:
                temp_res = []
                temp_nodes = []
                while queue:
                    cur = queue.pop(0)
                    temp_nodes.append(cur)
                    temp_res.append(cur.val)

                res.append(temp_res)

                for node in temp_nodes:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return res

    def display(self, cur, level):
        if cur is not None:
            self.display(cur.right, level + 1)
            print("    " * level + str(cur.val))
            self.display(cur.left, level + 1)


if __name__ == "__main__":
    s = Solution()
    root = [3, 9, 20, "null", "null", 15, 7]
    print(s.levelOrder(root))
    r = s.list2tree(root)
    s.display(r, 0)
    print(s.levelOrder2(r))
    print()

    root = [3, 9, 20, 6, "null", 15, 7, 1, 4, "null", "null", 87, "null", 34, 9]
    print(s.levelOrder(root))
    r = s.list2tree(root)
    s.display(r, 0)
    print(s.levelOrder2(r))

    root = [
        3,
        9,
        20,
        "null",
        "null",
        15,
        7,
        "null",
        "null",
        "null",
        "null",
        87,
        "null",
        34,
        9,
    ]
    print(s.levelOrder(root))
    r = s.list2tree(root)
    s.display(r, 0)
    print(s.levelOrder2(r))
