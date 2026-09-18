# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
      
        queue = deque() # we initialize a queue
        queue.append(root) # we append the root to the queue
        res = []  

        while queue: # while we have items in our queue
            length = len(queue) 
            level_block = []

            for i in range(length): # we add the items to the block
                node = queue.popleft() # we pop the item
                
                level_block.append(node.val) # we add it to the block

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            res.append(level_block)
        
        return res

        
        
        

# Step 1: Read the problem statement
    # We have a binary tree, and we want to return the level order traversal (as a nested list), from left to right.
    # 