class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, path = [], []
        used = [False] * len(nums) # used to keep track of whether the num is in path

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i] == True:
                    continue

                path.append(nums[i])
                used[i] = True

                backtrack()

                used[i] = False
                path.pop()
        
        backtrack()
        return result