class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        convert = set(nums)
        print(convert)
        max_length = {}
        for i in convert:
            k = i
            if (i-1) not in convert:
                max_length[i] = 1
            if (i-1) in convert and i+1 in convert:
                continue
            while k+1 in convert:
                print(i)
                max_length[i] += 1
                k = k + 1
                print(max_length)
        
        return max(max_length.values())