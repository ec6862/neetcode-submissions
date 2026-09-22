# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, maxValue):
            nonlocal count
            if not node:
                return None
            
            if node.val >= maxValue:
                count += 1
            
            newMax = max(node.val, maxValue)
            dfs(node.left, newMax)
            dfs(node.right, newMax)

            return None

        
        dfs(root, root.val)

        return count