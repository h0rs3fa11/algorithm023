
"""
解法1: 递归
比较两个链表当前节点的值的大小，将较小的一个作为新的根节点(node)，合并新链表(node.next)和另一个链表
终止条件是l1或l2任何一条链表已没有下一个节点
解法2: 迭代
使用迭代模拟递归的过程
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # # 解法1
        # # l1已遍历完成，返回剩下的l2
        # if not l1: return l2
        # # l2已遍历完成，返回剩下的l1
        # if not l2: return l1
        # if l1.val < l2.val:
        #     # l1值较小，将l1作为新的根节点，合并l1.next和l2
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     # 返回合并后的l1
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2
        # 解法2
        # 定义一个链表头
        p = phead = ListNode(-1)
        # 当l1和l2都不为None
        while l1 and l2:
            # p指向较小节点，较小节点的指针向后移动
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        # 循环结束后，l1和l2可能有一方不为None，将剩下的链表拼接到p上
        p.next = l1 if l1 else l2
        return phead.next
        