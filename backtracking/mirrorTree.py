# 给定一棵二叉树的根节点 root，请左右翻转这棵二叉树，并返回其根节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
# Display the tree in a hierarchical format.
def display(node=None, level=0):
    if node is not None:
        display(node.right, level + 1)
        print("    " * level + str(node.val))
        display(node.left, level + 1)

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root
    
if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print('original tree:')
    display(root)
    print()
    print('mirror tree:')
    display(Solution().mirrorTree(root))