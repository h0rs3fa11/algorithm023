#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 注意层序遍历是广度优先，迭代时不推荐用栈来维护，而用队列
        # 1. deque
        # from collections import deque
        # if not root: return []
        # deq = deque()
        # deq.append(root)
        # res = []
        # while deq:
        #     # 维护一个level，保存一个层级的所有节点val
        #     level = []
        #     for _ in range(len(deq)):
        #         root = deq.popleft()
        #         if root is not None:
        #             level.append(root.val)
        #         deq.extend(root.children)
        #     res.append(level)
        # return res

        # 与解法1类似，使用普通列表做队列
        if not root: return []
        queue, res = [root], []
        while queue:
            res.append(node.val for node in queue)
            queue = [c for node in queue for c in node.children]
        return res

# @lc code=end

