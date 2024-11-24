class BinaryTreeNode(object):
    def __init__(self, value):
        # TreeNode.__init__(self, value)
        self.value = value
        self.left = None
        self.right = None


# 找到两个节点的最低公共祖先
def lowestCommonAncestor(head, node1, node2):
    if not head:
        return None
    if head == node1 or head == node2:
        return head
    left = lowestCommonAncestor(head.left, node1, node2)
    right = lowestCommonAncestor(head.right, node1, node2)
    if left and right:  # 如果左右子树都找到了，说明找到了最低公共祖先，即当前结点
        return head
    return left or right  # 返回左节点和右节点不为None的节点


if __name__ == "__main__":
    # 创建一棵二叉树
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)

    # 找到两个节点的最低公共祖先
    node1 = root.left.left
    node2 = root.left.right
    lca = lowestCommonAncestor(root, node1, node2)
    print(lca.value)  # 输出结果：2

    node1 = root.left
    node2 = root.right.left
    lca = lowestCommonAncestor(root, node1, node2)
    print(lca.value)  # 输出结果：1
