class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(index, cur, total):
            if index >= len(nums) or total > target:
                return

            if total == target:
                res.append(cur.copy())
                return
            
            cur.append(nums[index])
            backtracking(index, cur, total + nums[index])
            cur.pop()
            backtracking(index+1, cur, total)

        backtracking(0, [], 0)
        return res