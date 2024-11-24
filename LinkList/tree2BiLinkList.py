

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left  # next
        self.right = right  # prev



class info(object):
    def __init__(self, start=None, end=None):
        # start and end are TreeNode object
        self.start = start
        self.end = end
        

# 将二叉树转换为双向链表
def tree2BiLinkList(root: TreeNode):
    if root is None:
        return info(None, None)
    leftHeadEnd = tree2BiLinkList(root.left)
    rightHeadEnd = tree2BiLinkList(root.right)
    
    if leftHeadEnd.end:
        leftHeadEnd.end.right = root
        
    root.left = leftHeadEnd.end
    root.right = rightHeadEnd.start
    
    if rightHeadEnd.start:
        rightHeadEnd.start.left = root
        
    S = leftHeadEnd.start if not leftHeadEnd.start else root
    E = rightHeadEnd.end if not rightHeadEnd.end else root
        
    return info(S, E)


def convert(head: TreeNode):
    if not head:
        return None
    return tree2BiLinkList(head).start


if __name__ == '__main__':
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(9))))
    print(convert(root))
    
    