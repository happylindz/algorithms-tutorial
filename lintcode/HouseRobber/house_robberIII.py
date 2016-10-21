# coding: utf8


'''

LintCode:http://www.lintcode.com/zh-cn/problem/house-robber-iii/

535. 打劫房屋 III:

在上次打劫完一条街道之后和一圈房屋之后，窃贼又发现了一个新的可以打劫的地方，但这次所有的房子组成的区域比较奇怪，聪明的窃贼考察地形之后，

发现这次的地形是一颗二叉树。与前两次偷窃相似的是每个房子都存放着特定金额的钱。你面临的唯一约束条件是：相邻的房子装着相互联系的防盗系统，

且当相邻的两个房子同一天被打劫时，该系统会自动报警。

算一算，如果今晚去打劫，你最多可以得到多少钱，当然在不触动报警装置的情况下。

样例:

  3
 / \
2   3
 \   \
  3   1

窃贼最多能偷窃的金钱数是 3 + 3 + 1 = 7.

    3
   / \
  4   5
 / \   \
1   3   1

窃贼最多能偷窃的金钱数是 4 + 5 = 9.

'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# 使用递归的方式去解决问题, 对于某个节点来说, 如果选了该节点, 那么其子节点就不能选了
# 所以我们用 result 在来存储该节点的两种状态, result[0] 代表选择了该节点所能获取到的最大利益(从下往上), result[1] 代表选择了不选择该节点
# 所能获取到的最大利益(从下往上)
# 不断递归, 自底向上



class Solution:
    # @param {TreeNode} root, the root of binary tree.
    # @return {int} The maximum amount of money you can rob tonight
    def houseRobber3(self, root):
        # write your code here
        result = self.postTraversal(root)
        return max(result[0], result[1])

    def postTraversal(self, node):
        result = [0, 0]
        if node == None:
            return result
        left = self.postTraversal(node.left)
        right = self.postTraversal(node.right)
        result[0] = left[1] + right[1] + node.val
        result[1] = max(left[0], left[1]) + max(right[0], right[1])
        return result

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s = Solution()
    print(s.houseRobber3(root))
