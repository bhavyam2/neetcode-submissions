class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def binarySearch(target):
            l, r = 0, n
            while l < r:
                m = (l+(r-1))//2
                if nums[m] >= target:
                    r = m
                else:
                    l = m +1
            return l
            
        ind = binarySearch(target)
        if ind == n or nums[ind] != target:
            return[-1, -1]
        return [ind, binarySearch(target + 1) - 1]
