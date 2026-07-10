class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1]
        prefix = 1
        for i in nums:
            arr.append(i*prefix)
            prefix = i * prefix
            if len(arr) > len(nums)-1:
                break
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            arr[i] = arr[i] * postfix
            postfix = postfix * nums[i]
        return arr