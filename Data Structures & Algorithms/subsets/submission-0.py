class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i): # 0, 1
            if i >= len(nums): # 0, 1, 2, 3 == True
                res.append(subset.copy()) # [1, 2, 3]
                print(f"subset is currently: {subset}")
                return
            # [1, 2, 3], [1, 2], [1, 3]
            print(f"We add choice: {nums[i]}")
            subset.append(nums[i]) # first adds the # [1, 2]
            dfs(i + 1)
            print(f"Returning from adding: {nums[i]}") 
            subset.pop()
            print(f"We do not add choice: {nums[i]}")
            dfs(i + 1) 

        dfs(0)

        return res