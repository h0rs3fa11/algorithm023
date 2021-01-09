#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # result = []
        # def inorder(node):
        #     if not node: return
        #     # 左根右的顺序
        #     inorder(node.left)
        #     result.append(node.val)
        #     inorder(node.right)

        # inorder(root)
        # return result

        # 迭代，维护一个栈
        # stack = []
        # result = []

        # while stack or root:
        #     if root:
        #         stack.append(root)
        #         root = root.left
        #     else:
        #         tmp = stack.pop()
        #         result.append(tmp.val)
        #         root = tmp.right
        # return result

        # 莫里斯遍历
        # 将树结构变成链表
        pre = None
        result = []
        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root
                tmp = root
                root = root.left
                tmp.left = None
            else:
                result.append(root.val)
                root = root.right
        return result

# @lc code=end

