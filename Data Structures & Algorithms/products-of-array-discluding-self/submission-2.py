class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1]
        postpre = 1
        for i in nums:
            arr.append(i*postpre)
            postpre = i * postpre
            if len(arr) > len(nums)-1:
                break
        postpre = 1
        for i in range(len(nums)-1, -1, -1):
            arr[i] = arr[i] * postpre
            postpre = postpre * nums[i]
        return arr