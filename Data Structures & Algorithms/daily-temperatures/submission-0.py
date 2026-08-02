class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while (len(stack) > 0) and t > stack[-1][0]:
                ans[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((t,i))
        return ans