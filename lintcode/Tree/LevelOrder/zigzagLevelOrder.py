# coding: utf8


'''

LintCode: http://www.lintcode.com/zh-cn/problem/binary-tree-zigzag-level-order-traversal/

71. 二叉树的锯齿形层次遍历

给出一棵二叉树，返回其节点值的锯齿形层次遍历（先从左往右，下一层再从右往左，层与层之间交替进行）

样例:

给出一棵二叉树 {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7
返回其锯齿形的层次遍历为：

[
  [3],
  [20,9],
  [15,7]
]

'''

# 这题和 levelOrder 1 类似, 需要用一个队列来管理每层节点, 难点在于如何做到有序输出, 所以我们需要用一个 tag 在标识是正向遍历还是反向遍历
# 并且在每次遍历完一层节点之后对 queue 进行反序

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def zigzagLevelOrder(root):
        # write your code here
        tag = True
        result, queue = [], [root]
        while len(queue) != 0:
            i, n = 0, len(queue)
            level = []
            while i < n:
                node = queue.pop(0)
                i += 1
                if node != None:
                    level.append(node.val)
                    if tag:
                        queue.append(node.left)
                        queue.append(node.right)
                    else:
                        queue.append(node.right)
                        queue.append(node.left)
            tag = not tag
            queue.reverse()
            if len(level) != 0:
                result.append(level)
        return result


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(zigzagLevelOrder(root))