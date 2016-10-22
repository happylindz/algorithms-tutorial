# coding: utf8

'''

LintCode:http://www.lintcode.com/zh-cn/problem/balanced-binary-tree/

93. 平衡二叉树

给定一个二叉树,确定它是高度平衡的。对于这个问题,一棵高度平衡的二叉树的定义是：一棵二叉树中每个节点的两个子树的深度相差不会超过1。

样例

给出二叉树 A={3,9,20,#,#,15,7}, B={3,#,20,15,7}

A)  3            B)    3
   / \                  \
  9  20                 20
    /  \                / \
   15   7              15  7

二叉树A是高度平衡的二叉树，但是B不是

'''

# 这题跟求最大二叉树的深度类似, 采用递归的方式求树的深度, 终止条件可以加入一个判断, 如果在递归当中发现了左右子树的高度差超过了 1, 可以返回 -1
# 这样在后续的递归就可以不用再继续判断. 已经有了 -1 就已经知道这棵树不平衡

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        return self.maxDepth(root) != -1

    def maxDepth(self, node):
        if node == None:
            return 0
        left_depth = self.maxDepth(node.left)
        right_depth = self.maxDepth(node.right)
        if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
            return -1
        return max(left_depth, right_depth) + 1