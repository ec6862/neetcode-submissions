class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, path = [], []

        def dfs(i, total):
            if total == target:
                result.append(path.copy())
                return
            
            if total > target or i >= len(nums):
                return
            
            # option 1: we use the number
            path.append(nums[i])
            dfs(i, total + nums[i])

            # option 2: we do not use the number
            path.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return result