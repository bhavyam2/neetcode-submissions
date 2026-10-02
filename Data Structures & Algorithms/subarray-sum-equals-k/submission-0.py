class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = { 0 : 1 }
        current_sum, count = 0, 0
        for n in nums:
            current_sum += n
            count += hashmap.get(current_sum - k, 0)
            hashmap[current_sum] = 1 + hashmap.get(current_sum, 0)
        return count