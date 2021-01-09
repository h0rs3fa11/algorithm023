#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # # 递归
        # if not root: return
        # print(root.val)
        # res = []
        # res.append(root.val)
        # for c in root.children:
        #     res.extend(self.preorder(c))
        # return res

        # 迭代
        if not root: return []
        stack, res = [root], []
        while stack:
            root = stack.pop()
            if root is not None:
                res.append(root.val)
            # 将子节点倒序放入栈，取出的时候就是正序
            for c in reversed(root.children):
                stack.append(c)
        return res
# @lc code=end

