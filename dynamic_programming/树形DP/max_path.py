# 求一棵树从根节点出发到达叶节点的路径和最大值(路径之和为经过节点的val值之和)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 全局变量，只在到达叶节点的时候有可能更新
max_sum = float("-inf")


def max_path_sum(root):
    global max_sum
    process1(root, 0)
    return max_sum


# 从根节点出发到达当前node节点上分的节点，获得的路径和
def process1(node, prev_path_sum):
    if node.left is None and node.right is None:
        global max_sum
        max_sum = max(max_sum, prev_path_sum + node.val)
        
    if node.left is not None:
        process1(node.left, prev_path_sum + node.val)

    if node.right is not None:
        process1(node.right, prev_path_sum + node.val)



def max_path_sum_2(node):
    if node.left is None and node.right is None:
        return node.val

    next = float("-inf")
    if node.left is not None:
        next = max_path_sum_2(node.left)

    if node.right is not None:
        next = max(next, max_path_sum_2(node.right))

    return node.val + next


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(3)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(10)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(7)
    root.right.left.left = TreeNode(5)
    root.right.right.right = TreeNode(3)
    
    print(max_path_sum(root))
    print(max_path_sum_2(root))

