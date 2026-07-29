class Solution:
    def trap(self, height: List[int]) -> int:
        current = 0
        l,r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        answer = 0
        while l < r:
            if lmax <= rmax:
                l += 1
                lmax = max(height[l], lmax)
                answer += lmax - height[l]
            else:
                r -= 1
                rmax = max(height[r], rmax)
                answer += rmax - height[r]

        return answer
