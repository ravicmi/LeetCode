# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not (root.left or root.right) : 
            return 0
        def dfs(node):
            l = 0
            r = 0 
            dl = 0
            dr = 0 
            if node.left  :
                l, dl = dfs(node.left)
                l += 1
                
            if node.right : 
                r, dr = dfs(node.right)
                r += 1
            dn = max(l+r, max(dl, dr))

            return max(l,r), dn
        
        return dfs(root)[1]
        # left_depth = 0 
        # if root.left: 
        #     left_depth = dfs(root.left) +1
        # right_depth = 0
        # if root.right:
        #     right_depth = dfs(root.right) +1
        # return left_depth + right_depth

