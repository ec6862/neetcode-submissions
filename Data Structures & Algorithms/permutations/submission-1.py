class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, path = [], []
        used = [False] * len(nums) # used to keep track of whether the num is in path

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                print(f"adding path: {path[:]}")
                return
            
            print(f"new for loop: {path}")
            for i in range(len(nums)):
                if used[i] == True:
                    print(f"{nums[i]} already in path: {path}")
                    continue

                path.append(nums[i])
                used[i] = True
                print(f"i is: {i}, adding {nums[i]} to path, backtracking")

                backtrack()

                used[i] = False
                path.pop()
                print(f"removing {nums[i]}, path: {path}")
        
        backtrack()
        return result