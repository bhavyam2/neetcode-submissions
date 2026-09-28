class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        maxL, maxR = 0, 0
        total = 0
        while l < r:
            maxL = max(height[l], maxL)
            maxR = max(height[r], maxR)
            if height[l] < height[r]:
                total += maxL - height[l]
                l += 1
            else:
                total += maxR- height[r]
                r -= 1
        return total