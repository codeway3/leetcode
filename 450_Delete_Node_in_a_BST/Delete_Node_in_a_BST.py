"""https://leetcode.com/problems/delete-node-in-a-bst/description/"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 整体思路不够清晰 而且增加了一个函数 建议参考下面的解法
    def insertNode(self, root, node):
        if not node:
            pass
        elif not root:
            root = node
        elif node.val < root.val:
            root.left = self.insertNode(root.left, node)
        elif node.val > root.val:
            root.right = self.insertNode(root.right, node)
        return root

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if key == root.val:
            tmp = root.left
            if not tmp:
                return root.right
            else:
                tmp.right = self.insertNode(root.right, tmp.right)
                root = tmp
                return root
        else:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            else:
                root.right = self.deleteNode(root.right, key)
            return root


# others solution
"""
def deleteNode(root, key):
if not root: # if root doesn't exist, just return it
    return root
if root.val > key: # if key value is less than root value, find the node in the left subtree
    root.left = deleteNode(root.left, key)
elif root.val < key: # if key value is greater than root value, find the node in right subtree
    root.right= deleteNode(root.right, key)
else: #if we found the node (root.value == key), start to delete it
    if not root.right: # if it doesn't have right children, we delete the node then new root would be root.left
        return root.left
    if not root.left: # if it has no left children, we delete the node then new root would be root.right
        return root.right
            # if the node have both left and right children,  we replace its value with the minmimum value in the right subtree and then delete that minimum node in the right subtree
    temp = root.right
    mini = temp.val
    while temp.left:
        temp = temp.left
        mini = temp.val
    root.val = mini # replace value
    root.right = deleteNode(root.right,root.val) # delete the minimum node in right subtree
return root
"""
