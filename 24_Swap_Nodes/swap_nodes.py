"""
https://leetcode.com/problems/swap-nodes-in-pairs/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        node = ListNode(None)
        node = head.next
        if node is None:
            return head
        head.next = self.swapPairs(node.next)
        node.next = head
        return node


# others solution
"""
Here, pre is the previous node. Since the head doesn’t have a previous node, I just use self instead. Again, a is the current node and b is the next node.

To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next, we need to change those three references. Instead of thinking about in what order I change them, I just change all three at once.

def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next
pre这个指向很巧妙 不用新建node了
用非多变量赋值来做时注意逻辑关系
"""
