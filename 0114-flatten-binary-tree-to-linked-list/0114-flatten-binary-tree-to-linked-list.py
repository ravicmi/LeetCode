# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        if not root.left:
            self.flatten(root.right)
            return
        if not root.right:
            root.right = root.left
            root.left = None
            self.flatten(root.right)
            return
        l = root.left
        while l.right:
            l = l.right
        l.right= root.right
        self.flatten(root.left)
        root.right =  root.left
        root.left = None
        return
        