class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]        
        def helper(houses):
            if len(houses) == 1:
                return houses[0]

            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                skip = dp[i - 1]
                rob = houses[i] + dp[i - 2]
                dp[i] = max(skip, rob)

            return dp[-1]

        return max(helper(nums[1:]), helper(nums[:-1]))
        
            
