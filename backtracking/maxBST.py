# 找到一棵二叉树的最大二叉搜索子树的头节点

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class info(object):
    def __init__(self, maxBSTHead, maxBSTSize, isBST, min, max):
        self.maxBSTHead = maxBSTHead
        self.maxBSTSize = maxBSTSize
        self.isBST = isBST
        self.min = min
        self.max = max
        

def maxBST(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return None
    
    leftInfo = maxBST(root.left)
    rightInfo = maxBST(root.right)
    
    min_val = root.val
    max_val = root.val
    if root.left:
        min_val = min(min_val, root.left.val)
        max_val = max(max_val, root.left.val)
    if root.right:
        min_val = min(min_val, root.right.val)
        max_val = max(max_val, root.right.val)
        
    maxBSTHead = None
    maxBSTSize = 0
    if leftInfo:
        maxBSTHead = leftInfo.maxBSTHead
        maxBSTSize = leftInfo.maxBSTSize

    if rightInfo and rightInfo.maxBSTSize > maxBSTSize:
        maxBSTHead = rightInfo.maxBSTHead
        maxBSTSize = rightInfo.maxBSTSize
        
    isBST = False
    
    if (leftInfo is None or leftInfo.isBST) and (rightInfo is None or rightInfo.isBST):
        if (leftInfo is None or leftInfo.max < root.val) and (rightInfo is None or rightInfo.min > root.val):
            isBST = True
            maxBSTHead = root
            maxBSTSize = 1 + (0 if leftInfo is None else leftInfo.maxBSTSize) + (0 if rightInfo is None else rightInfo.maxBSTSize)
    
    return info(maxBSTHead, maxBSTSize, isBST, min_val, max_val)
    
    
if __name__ == '__main__':
    root = TreeNode(4, TreeNode(2, TreeNode(8), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(9))))
    # root.right.right.right = TreeNode(8)
    print(maxBST(root).maxBSTHead.val)