from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        for r, values in enumerate(nums):
            if r >= k and q and q[0] == nums[r-k]:
                q.popleft()
            
            while q and q[-1] < values:
                q.pop()
            
            q.append(values)

            if r >= k -1:
                output.append(q[0])
        return output
            

