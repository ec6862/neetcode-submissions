class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        
        sortedMap = sorted(hashMap.items(), key=lambda item:item[1], reverse=True)
        res = []
        for i in range(k):
            key, value = sortedMap[i]
            res.append(key)

        return res