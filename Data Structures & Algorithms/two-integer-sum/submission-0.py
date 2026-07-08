class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = {}
        i = 0
        for n in nums:            
            diff = target - n
            if diff in answer:
                return [answer[diff], i]
            answer[n] = i
            i = i + 1


