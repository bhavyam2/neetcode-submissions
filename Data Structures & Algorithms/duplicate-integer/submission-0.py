class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = defaultdict(list)
        for i in nums:
            answer[i].append(i)

        for x in answer.values():
            if (len(x) > 1):
               return True
        return False