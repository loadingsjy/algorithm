# This code is used to solve the problem of pre-order and in-order traversal to get the post-order traversal.
# 根据一棵二叉树的前序遍历和中序遍历，求后序遍历。（树种没有重复节点）


def PreIn2Post(preorder, inorder):
    if not preorder or not inorder:
        return []
    root = preorder[0]
    root_index = inorder.index(root)
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1 :]
    left_preorder = preorder[1 : root_index + 1]
    right_preorder = preorder[root_index + 1 :]

    left_postorder = PreIn2Post(left_preorder, left_inorder)
    right_postorder = PreIn2Post(right_preorder, right_inorder)
    return left_postorder + right_postorder + [root]


def PreIn2Post_v2(
    preorder, inorder, postorder, pre_s, pre_e, in_s, in_e, post_s, post_e
):
    if pre_s > pre_e:
        return
    if pre_s == pre_e:
        postorder[post_s] = preorder[pre_s]
        # return

    postorder[post_e] = preorder[pre_s]     # 前序遍历的开始（根节点）是后序遍历的结束
    
    root_index = in_s
    for root_index in range(in_s, in_e + 1):
        if preorder[pre_s] == inorder[root_index]:
            break
    
    PreIn2Post_v2(
        preorder,
        inorder,
        postorder,
        pre_s + 1,
        pre_s + root_index - in_s,
        in_s,
        root_index - 1,
        post_s,
        post_s + root_index - in_s - 1,
    )
    PreIn2Post_v2(
        preorder,
        inorder,
        postorder,
        pre_s + root_index - in_s + 1,
        pre_e,
        root_index + 1,
        in_e,
        post_s + root_index - in_s,
        post_e - 1,
    )


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    postorder = PreIn2Post(preorder, inorder)
    print(postorder)  # Output: [9, 15, 7, 20, 3]
    postorder = [0] * len(preorder)
    PreIn2Post_v2(preorder, inorder, postorder, 0, len(preorder) - 1, 0, len(inorder) - 1, 0, len(preorder) - 1)
    print(postorder)  # Output: [9, 15, 7, 20, 3]
