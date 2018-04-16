"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        elif not head.next:
            return TreeNode(head.val)  # 注意rtype是TreeNode，要利用ListNode的val创建新实例
        # 此处为了寻找原链表的中间节点，使用两个步距不一样的指针
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tmp, slow.next = slow.next, None
        now = TreeNode(tmp.val)  # 构造新节点，递归调用该函数，生成左右子树
        now.left = self.sortedListToBST(head)
        now.right = self.sortedListToBST(tmp.next)
        return now
