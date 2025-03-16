# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, leading):
            leading = leading*10+node.val
            total = 0
            if node.left: 
                total += dfs(node.left, leading)
            if node.right:
                total += dfs(node.right, leading)
            if (not node.left) and (not node.right):
                total = leading
            return total
        return dfs(root, 0)
        