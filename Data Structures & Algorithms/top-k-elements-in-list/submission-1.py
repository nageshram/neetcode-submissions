class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        res =set()

        for i in range(len(nums)):
            counter[nums[i]] = counter.get(nums[i], 0) +1
            
        res = sorted(counter.keys(), key= lambda x : counter[x], reverse=True)
        return list(res[:k])
