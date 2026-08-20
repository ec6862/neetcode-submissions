# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:        
        def dfs(root):
            if not root:
                return (True, 0)
            
            left_balance, left_height = dfs(root.left)
            right_balance, right_height = dfs(root.right)

            is_balanced = (abs(left_height - right_height) <= 1 and
                left_balance == True and
                right_balance == True)
            
            return (is_balanced, 1 + max(left_height, right_height))

        balance, height = dfs(root)

        return balance