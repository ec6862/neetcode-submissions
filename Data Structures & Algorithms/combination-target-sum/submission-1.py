class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, curr = [], []

        def dfs(i, total):
            if total == target:
                res.append(curr[:])
                return

            if total > target or i == len(nums):
                return
            
            # include the num
            curr.append(nums[i])
            dfs(i, total + nums[i])
            # go to next number
            curr.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)

        return res