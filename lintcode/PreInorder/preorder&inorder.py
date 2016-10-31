'''

LintCode: http://www.lintcode.com/zh-cn/problem/construct-binary-tree-from-preorder-and-inorder-traversal/

73. 前序遍历和中序遍历树构造二叉树:

根据前序遍历和中序遍历树构造二叉树.

样例:

给出中序遍历：[1,2,3]和前序遍历：[2,1,3]. 返回如下的树:

  2
 / \
1   3

'''

# 递归
# 前序遍历的第一个节点为该树的根节点，然后从中序遍历中查找这个节点，在这个节点的前半部分为该树的左子树， 这个节点的后半部分为该树的右子树
# 将数组不断切分，即可获得该树


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        return self.build(preorder, inorder)
       
    def build(self, preorder, inorder):
        node = None
        if len(preorder) == 0:
            pass
        elif len(preorder) == 1:
            node = TreeNode(preorder[0])
        else:
            node = TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            left_in = inorder[0:index]
            right_in = inorder[index + 1:]
            n = len(left_in)
            left_pre = preorder[1:1 + n]
            right_pre = preorder[1 + n:]
            node.left = self.build(left_pre, left_in)
            node.right = self.build(right_pre, right_in)
        return node