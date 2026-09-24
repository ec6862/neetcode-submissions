class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        maxCount = 0
        for num in nums:
            hashSet.add(num)

        for num in nums:
            count = 0
            if num - 1 not in hashSet: # if there is no preceding number
                count = 1
                sub = num + 1
                while sub in hashSet:
                    count += 1
                    sub += 1
            maxCount = max(maxCount, count)
        
        return maxCount
