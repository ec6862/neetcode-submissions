class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result, comb = [], []
        candidates.sort()
        def dfs(i, total):
            if total == target:
                result.append(comb.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            # option 1: we take the number
            comb.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            # option 2: we do not take the number
            comb.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)
        return result