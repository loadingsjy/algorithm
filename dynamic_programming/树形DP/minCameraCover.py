# 给定一个二叉树，我们在树的节点上安装摄像头。
# 节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
# 计算监控树的所有节点所需的最小摄像头数量。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minCameraCover_greedy(root) -> int:
    result = 0

    # 后序遍历二叉树
    # 如果左右孩子都被覆盖，则当前节点不用安装摄像头；
    # 如果左右孩子至少有一个没有覆盖，则当前节点需要安装摄像头；
    # 如果左右孩子至少有一个摄像头，则当前节点不需要安装摄像头；
    # 最后遍历到根节点，根节点没有被覆盖那么根节点需要再安装一个摄像头；
    def postorder_traverse(node):
        nonlocal result
        # 0: 没有被摄像头覆盖
        # 1: 有摄像头
        # 2: 没有摄像头，但被摄像头覆盖
        if node is None:
            return 2
        left = postorder_traverse(node.left)
        right = postorder_traverse(node.right)
        if left == 2 and right == 2:
            return 0
        # 条件2和条件3不能交换顺序，不然会有bug
        if left == 0 or right == 0:
            # print(node.val)
            result += 1
            return 1
        if left == 1 or right == 1:
            return 2

    # 如果根节点没有被覆盖，则需要安装摄像头
    if postorder_traverse(root) == 0:
        result += 1
    return result


def minCameraCover_dp(root) -> int:
    """每个节点有三种可能状态：安装摄像头、不安装摄像头但在他的父节点安装摄像头、不安装摄像头但在他的儿子节点安装摄像头"""

    def dfs(node):
        if node is None:
            return float("inf"), 0, 0

        l_choosed, l_by_fa, l_by_child = dfs(node.right)
        r_choosed, r_by_fa, r_by_child = dfs(node.left)
        # child一定大于等于fa
        choosed = (min(l_choosed, l_by_fa) + min(r_choosed, r_by_fa) + 1)
        choose_fa = min(l_choosed, l_by_child) + min(r_choosed, r_by_child)
        choose_child = min(l_choosed + r_by_child, r_choosed + l_by_child, l_choosed + r_choosed)

        return choosed, choose_fa, choose_child
    choose, _, by_child = dfs(root)
    return min(choose, by_child)
    


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    root.right.right.right = TreeNode(14)

    root.left.left.left = TreeNode(8)
    root.left.left.left.left = TreeNode(9)
    root.left.left.left.right = TreeNode(10)
    root.left.left.left.left.left = TreeNode(11)
    root.left.left.left.left.left.left = TreeNode(12)
    root.left.left.left.left.left.left.left = TreeNode(13)
    
    print(minCameraCover_greedy(root))
    print(minCameraCover_dp(root))
