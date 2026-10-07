import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dictionary = defaultdict(int)
        for i in nums:
            dictionary[i] += 1

        heap = []
        for num in dictionary.keys():
            heapq.heappush(heap, (dictionary[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res