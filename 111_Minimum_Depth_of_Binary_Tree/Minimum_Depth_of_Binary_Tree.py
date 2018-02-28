"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getminDepth(rt):
            if not rt:
                return 0
            # 注意这里 要考虑到 题目要求的是到【叶子节点】的距离为深度
            if not rt.left or not rt.right:
                return getminDepth(rt.left) + getminDepth(rt.right) + 1
            return min(getminDepth(rt.left), getminDepth(rt.right)) + 1
        return getminDepth(root)


# others solutions
# 大概都是这个思路 要细心考虑所有可能的情况
