# coding:utf8

'''

LintCode: http://www.lintcode.com/zh-cn/problem/binary-tree-level-order-traversal-ii/

70. 二叉树的层次遍历 II

给出一棵二叉树，返回其节点值从底向上的层次序遍历（按从叶节点所在层到根节点所在的层遍历，然后逐层从左往右遍历）

样例:

给出一棵二叉树 {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7
按照从下往上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

'''



class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# 方法一: 可以用一个投机取巧的方式, 将之前 levelOrder I 的输出结果反向排序, 即为所求结果


def levelOrder1(root):
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
    return result[::-1]

# 每次插入结果时都插入到结果集的头部


def levelOrder2(root):
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
            result.insert(0, level)
    return result

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(levelOrder2(root))
