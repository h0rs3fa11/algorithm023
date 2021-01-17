#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # # 1 递归
        # # 终止条件
        # if not (preorder and inorder): return
        # # 从前序序列获取根节点
        # root = TreeNode(preorder[0])
        # # 获取根节点在中序序列的位置，左边的是左子树，右边的是右子树
        # index = inorder.index(preorder[0])
        # # 递归
        # root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        # root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        # return root

        # 2.另一种写法
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            # 因为用pop取的前序根节点，preorder中已经删除根节点，所以preorder不用变
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root     

        
# @lc code=end

