# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
# 除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
# 给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root):
    # dp[0]表示不偷当前节点的最大收益，dp[1]表示偷当前节点的最大收益
    if not root:
        return 0, 0

    # 后序遍历，递归计算左右子树的最大收益
    left_dp = postorderTraversal(root.left)
    right_dp = postorderTraversal(root.right)
    # 选择偷当前节点，子节点必须不偷
    val1 = left_dp[0] + right_dp[0] + root.val
    # 选择不偷当前节点，子节点可偷可不偷，选择两种情况最大值
    val2 = max(left_dp[0], left_dp[1]) + max(right_dp[0], right_dp[1])
    return val2, val1


def rob(root: TreeNode) -> int:
    return max(postorderTraversal(root))
        

if __name__ == '__main__':
    root = TreeNode(3, TreeNode(2, TreeNode(3), TreeNode(3)), TreeNode(3, None, TreeNode(1)))
    print(rob(root)) # 7
    

    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
    print(rob(root)) # 9