#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # res = []
        # def dfs(node):
        #     if not node: return
        #     res.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return res

        # 迭代
        # res = []
        # stack = []
        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         res.append(root.val)
        #         root = root.left
        #     root = stack.pop()
        #     root = root.right
        # return res

# @lc code=end

