class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur = [], []
        sortedNums = sorted(candidates)

        def dfs(i, total):
            if total == target:
                res.append(cur[:])
                return
            
            if i == len(candidates) or total > target:
                return
            
            cur.append(sortedNums[i])
            dfs(i + 1, total + sortedNums[i])
            cur.pop()

            while i + 1 < len(candidates) and sortedNums[i] == sortedNums[i + 1]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)
        return res