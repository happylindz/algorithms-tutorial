# coding: utf8

'''
LintCode:

69. 二叉树的层次遍历: http://www.lintcode.com/zh-cn/problem/binary-tree-level-order-traversal/

给出一棵二叉树，返回其节点值的层次遍历（逐层从左往右访问）

样例:
给一棵二叉树 {3,9,20,#,#,15,7} ：

  3
 / \
9  20
  /  \
 15   7
返回他的分层遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def levelOrder(root):
    result = []
    queue = [root]
    while len(queue) != 0:
        i, n = 0, len(queue)
        level = []
        while i < n:
            node = queue.pop(0)
            if node != None:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            i += 1
        if len(level) != 0:
            result.append(level)
    return result


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(0)
    print(levelOrder(root))
