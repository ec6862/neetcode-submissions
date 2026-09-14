# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(root):
            if not root:
                return [0, True]
            
            left_height, left_balance = balanced(root.left)
            right_height, right_balance = balanced(root.right)

            if left_balance == False or right_balance == False or abs(left_height - right_height) > 1:
                balancedTree = False
            else:
                balancedTree = True
            
            return [1 + max(left_height, right_height), balancedTree]
            
        height, balance = balanced(root)

        return balance