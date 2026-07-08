class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums) 
        suffix = [1] * len(nums)
        multiple = 1
        for pre in range (1,len(nums)):
            multiple *= nums[pre-1]
            prefix[pre] = multiple
        print(prefix)
        multiple = 1
        for suff in range (len(nums) - 1, 0, -1):
            multiple *= nums[suff]
            suffix[suff - 1] = multiple
        print(suffix)
        answer = [1]*len(nums)
        for i in range(0, len(nums)):
            answer[i] = prefix[i]*suffix[i]
        return answer