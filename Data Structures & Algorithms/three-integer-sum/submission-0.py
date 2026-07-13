class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:    
        indice = 0
        answer = []
        sort = sorted(nums)
        print(sort)
        for i,value in enumerate(sort):
            if value > 0:
                break
            if i > 0 and value == sort[i - 1]:
                continue
            l, r = i+1, len(sort) - 1
            while l < r:
                sums = value + sort[l] + sort[r]
                if sums < 0:
                    l += 1
                elif sums > 0:
                    r -= 1
                else:
                    answer.append([value, sort[l], sort[r]])
                    l += 1
                    r -= 1
                    while l < r and sort[l] == sort[l-1]:
                        l += 1
                
            
        return answer
