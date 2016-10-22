# coding:utf8

'''
LintCode: http://www.lintcode.com/zh-cn/problem/maximum-depth-of-binary-tree/

97. 二叉树的最大深度

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的距离。

样例
给出一棵如下的二叉树:

  1
 / \
2   3
   / \
  4   5
这个二叉树的最大深度为3.


'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# 递归

def max_depth_with_recursion(root):
    if root == None:
        return 0
    left_depth = max_depth_with_recursion(root.left)
    right_depth = max_depth_with_recursion(root.right)
    return max(left_depth, right_depth) + 1


# 迭代

def max_depth_with_iterative(root):
    queue = []
    queue.append(root)
    max_depth = 0
    while len(queue) != 0:
        n = len(queue)
        for i in range(n):
            node = queue.pop(0)
            if node == None:
                continue
            else:
                queue.append(node.left)
                queue.append(node.right)
        if len(queue) != 0:
            max_depth += 1
    return max_depth
