class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        arr = []

        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 0
            hashMap[nums[i]] += 1

        sorted_by_values = sorted(hashMap.items(), key=lambda item:item[1], reverse=True)
        for i in range(k):
            key, value = sorted_by_values[i]
            arr.append(key)

        return arr