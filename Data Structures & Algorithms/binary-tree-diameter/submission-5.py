# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        def dfs(root):
            if not root:
                return 0
            
            print(f"We are at node {root.val}, doing left and right")
            left = dfs(root.left)
            right = dfs(root.right)
            self.maxDiameter = max(self.maxDiameter, left + right)
            print(f"Finished traversing left and right of node {root.val}. Left: {left}, right: {right}")
            return 1 + max(left, right)
        dfs(root)
        return self.maxDiameter