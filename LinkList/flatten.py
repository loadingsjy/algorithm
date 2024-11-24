# 二叉树展开为链表
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：
# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。

from reverseList import ListNode, create_list_node
from copy import deepcopy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_list(head):
    cur = head
    while cur is not None:
        print(cur.val, end=",  ")
        cur = cur.right
    print()


def display(current_node, level):
    if current_node is not None:
        display(current_node.right, level + 1)
        print("    " * level + str(current_node.val))
        display(current_node.left, level + 1)


class Solution:

    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        stack = [root]
        prev = None

        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = curr

    def flatten2(self, root) -> None:
        preorderList = list()
        stack = list()
        node = root

        while node or stack:
            while node:
                preorderList.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr

    def flatten_re(self, root):
        preorderList = list()

        def preorderTraversal(root):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)

        preorderTraversal(root)
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr

    def flatten_pre(self, root) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    root.left.left.left = TreeNode(8)
    root.right.right.right = TreeNode(9)
    root.left.left.left.left = TreeNode(10)
    root.left.left.left.right = TreeNode(11)
    display(root, 0)

    s = Solution()

    r1 = deepcopy(root)
    s.flatten(r1)
    print_list(r1)

    r2 = deepcopy(root)
    s.flatten2(r2)
    print_list(r2)

    r3 = deepcopy(root)
    s.flatten_re(r3)
    print_list(r3)

    r4 = deepcopy(root)
    s.flatten_pre(r4)
    print_list(r4)
