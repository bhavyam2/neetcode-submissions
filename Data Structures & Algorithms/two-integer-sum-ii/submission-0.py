class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        answer = []
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
                print('right')
                print(right)
            if numbers[left] + numbers[right] < target:
                left += 1
                print('left')
                print(left)
            if numbers[left] + numbers[right] == target:
                answer.append(int(left+1))
                answer.append(int(right+1))
                return answer