


class node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 求以node为根节点的完全二叉树的最大深度, level为当前节点的深度
def most_left_level(node,level=0):
    while node:
        level += 1
        node = node.left
    return level - 1


def bs(node, level, h):
    if level == h:
        return 1
    if most_left_level(node.right,level+1) == h:    # 右子树的最左节点深度为h,则左子树为完全二叉树，递归处理右子树
        return (1<<(h-level)) + bs(node.right, level+1, h)
    else:       # 右子树的最左节点深度为h-1,则右子树为完全二叉树，递归处理左子树
        return (1<<(h-level-1)) + bs(node.left, level+1, h)

    
# 求完全二叉树节点的个数
def completeTreeNodeNumber(root):
    if not root:
        return 0
    h = most_left_level(root)
    return bs(root, 0, h)



if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)
    root.left.left.left = node(8)
    root.left.left.right = node(9)
    root.left.right.left = node(10)
    root.left.right.right = node(11)
    root.right.left.left = node(12)
    root.right.left.right = node(13)
    root.right.right.left = node(14)
    root.right.right.right = node(15)
    print(completeTreeNodeNumber(root)) # 15