# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def sub_prob(node, low, high):
            if node.val < low : 
                if node.right: 
                    return sub_prob(node.right, low, high)
                else: 
                    return 0 
            if node.val > high:
                if node.left:
                    return sub_prob(node.left, low, high)
                else: 
                    return 0 
            left_sum = sub_prob(node.left, low, high) if node.left else 0 
            right_sum = sub_prob(node.right, low, high) if node.right else 0 
            return node.val + left_sum + right_sum
        return sub_prob(root, low, high)